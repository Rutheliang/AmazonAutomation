from selenium.webdriver.common.by import By


class CartCheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    CART = (By.CSS_SELECTOR, "input[id='add-to-cart-button']")
    CHECKOUT = (By.CSS_SELECTOR, "input[name='proceedToRetailCheckout']")

    def go_to_checkout(self):
        self.driver.find_element(*CartCheckoutPage.CART).click()
        self.driver.find_element(*CartCheckoutPage.CHECKOUT).click()
