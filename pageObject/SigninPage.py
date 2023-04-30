from selenium.webdriver.common.by import By


class SigninPage:

    def __init__(self, driver):
        self.driver = driver

    SIGNIN_EMAIL = (By.ID, "ap_email")
    SIGNIN_BUTTON = (By.CSS_SELECTOR, ".a-button-input")
    PASSWORD = (By.ID, "ap_password")
    PASSWORD_BUTTON = (By.ID, "signInSubmit")
    AMAZON_LOGO = (By.CSS_SELECTOR, "i[class='a-icon a-icon-logo']")

    def user_signin(self, signinData):
        self.driver.find_element(*SigninPage.SIGNIN_EMAIL).send_keys(signinData["email"])
        self.driver.find_element(*SigninPage.SIGNIN_BUTTON).click()
        self.driver.find_element(*SigninPage.PASSWORD).send_keys(signinData["password"])
        self.driver.find_element(*SigninPage.PASSWORD_BUTTON).click()
        self.driver.find_element(*SigninPage.AMAZON_LOGO).click()







