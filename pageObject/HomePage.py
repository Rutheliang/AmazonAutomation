from selenium.webdriver.common.by import By


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    SEARCH = (By.ID, "twotabsearchtextbox")
    ITEMS = (By.CSS_SELECTOR, "div[class='s-suggestion s-suggestion-ellipsis-direction']")
    SELECTED = (By.ID, "twotabsearchtextbox")
    HOVER = (By.CSS_SELECTOR, "span[id*='accountList']")
    REGISTER = (By.CSS_SELECTOR, "a[href*='https://www.amazon.com/ap/register?openid.pape.max']")

    def search_item(self):
        self.driver.find_element(*HomePage.SEARCH).send_keys("roblox")
        # self.driver.find_element(By.ID, "twotabsearchtextbox")

    def get_items(self):
        return self.driver.find_elements(*HomePage.ITEMS)
        # self.driver.find_elements(By.CSS_SELECTOR, "div[class='s-suggestion s-suggestion-ellipsis-direction']")

    def item_selected(self):
        return self.driver.find_element(*HomePage.SELECTED)
        # self.driver.find_element(By.ID, "twotabsearchtextbox").get_attribute("value")

    def hover_signin(self):
        return self.driver.find_element(*HomePage.HOVER)
        # action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, "span[id*='accountList']")).perform()

    def register_link(self):
        self.driver.find_element(*HomePage.REGISTER).click()
        # self.driver.find_element(By.CSS_SELECTOR, "a[href*='https://www.amazon.com/ap/register?openid.pape.max']").click()