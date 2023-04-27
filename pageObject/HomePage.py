from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    SEARCH = (By.ID, "twotabsearchtextbox")
    ITEMS = (By.CSS_SELECTOR, "div[class='s-suggestion s-suggestion-ellipsis-direction']")
    VALUE = (By.ID, "twotabsearchtextbox")
    HOVER = (By.CSS_SELECTOR, "span[id*='accountList']")
    START = (By.CSS_SELECTOR, "a[href*='https://www.amazon.com/ap/register?openid.pape.max']")

    def getSearch(self):
        return self.driver.find_element(*HomePage.SEARCH)
        # self.driver.find_element(By.ID, "twotabsearchtextbox")

    def getItems(self):
        return self.driver.find_elements(*HomePage.ITEMS)
        # self.driver.find_elements(By.CSS_SELECTOR, "div[class='s-suggestion s-suggestion-ellipsis-direction']")

    def getValue(self):
        return self.driver.find_element(*HomePage.VALUE)
        # self.driver.find_element(By.ID, "twotabsearchtextbox").get_attribute("value")

    def getHover(self):
        return self.driver.find_element(*HomePage.HOVER)
        # action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "span[id*='accountList']")).perform()

    def getStart(self):
        return self.driver.find_element(*HomePage.START)
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='https://www.amazon.com/ap/register?openid.pape.max']").click()