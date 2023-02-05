from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    search = (By.ID, "twotabsearchtextbox")
    items = (By.CSS_SELECTOR, "div[class='s-suggestion s-suggestion-ellipsis-direction']")
    value = (By.ID, "twotabsearchtextbox")
    hover = (By.CSS_SELECTOR, "span[id*='accountList']")
    start = (By.CSS_SELECTOR, "a[href*='https://www.amazon.com/ap/register?openid.pape.max']")

    def getSearch(self):
        return self.driver.find_element(*HomePage.search)
        # self.driver.find_element(By.ID, "twotabsearchtextbox")

    def getItems(self):
        return self.driver.find_elements(*HomePage.items)
        # self.driver.find_elements(By.CSS_SELECTOR, "div[class='s-suggestion s-suggestion-ellipsis-direction']")

    def getValue(self):
        return self.driver.find_element(*HomePage.value)
        # self.driver.find_element(By.ID, "twotabsearchtextbox").get_attribute("value")

    def getHover(self):
        return self.driver.find_element(*HomePage.hover)
        # action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "span[id*='accountList']")).perform()

    def getStart(self):
        return self.driver.find_element(*HomePage.start)
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='https://www.amazon.com/ap/register?openid.pape.max']").click()