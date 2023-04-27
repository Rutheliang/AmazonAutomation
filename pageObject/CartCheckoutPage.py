from selenium.webdriver.common.by import By


class CartCheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    CART = (By.CSS_SELECTOR, "input[id='add-to-cart-button']")
    CHECKOUT = (By.CSS_SELECTOR, "input[name='proceedToRetailCheckout']")

    def getCart(self):
        return self.driver.find_element(*CartCheckoutPage.CART)
        # self.driver.find_element(By.CSS_SELECTOR, "input[id='add-to-cart-button']")

    def getCheckout(self):
        return self.driver.find_element(*CartCheckoutPage.CHECKOUT)
        # self.driver.find_element(By.CSS_SELECTOR, "input[name='proceedToRetailCheckout']")