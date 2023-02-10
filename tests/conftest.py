import pytest
from selenium import webdriver

driver = None  # need for the screenshot -> def _capture_screenshot(name):

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):  # give this step to return driver / no need to return driver
    global driver
    browser_name = request.config.getoption("browser_name")  # retrieve command line value (browser)
    if browser_name == "chrome":
        chrome_options = Options()
        chrome_options.add_experimental_option("detach", True)
        service_obj = Service("/Users/ruthelia/Downloads/chromedriver")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)
    elif browser_name == "firefox":
        service_obj = Service("/Users/ruthelia/Downloads/geckodriver 2")
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "IE":
        print("IE driver")

    driver.get("https://www.amazon.com")
    driver.maximize_window()
    driver.implicitly_wait(5)
    request.cls.driver = driver  # give this step to return driver / no need to return
    yield
    driver.close()


@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


def _capture_screenshot(name):
    driver.get_screenshot_as_file(name)
