from selenium.webdriver.common.by import By


class SearchItemPage:

    def __init__(self, driver):
        self.driver = driver

    PRICE = (By.XPATH, "//li[@id='p_36/1253561011']")
    AGE = (By.XPATH, "//li[@aria-label='5 to 7 Years']/span/a/div")
    SELECT = (By.XPATH, "//div[@data-component-type='s-search-result'][2]")
    MATERIAL = (By.XPATH, "//li[@aria-label='Plastic']")

    def add_selected_item_to_cart(self):
        self.driver.find_element(*SearchItemPage.PRICE).click()
        self.driver.find_element(*SearchItemPage.AGE).click()
        self.driver.find_element(*SearchItemPage.MATERIAL).click()
        self.driver.find_element(*SearchItemPage.SELECT).click()

