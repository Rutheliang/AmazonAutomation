from selenium.webdriver.common.by import By


class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver

    NAME = (By.ID, "ap_customer_name")
    EMAIL = (By.ID, "ap_email")
    PASSWORD = (By.ID, "ap_password")
    RE_ENTER_PASSWORD = (By.ID, "ap_password_check")
    CREATE_ACCOUNT_BUTTON = (By.ID, "continue")
    PW_MISMATCH = (By.XPATH, "//div[@id='auth-password-mismatch-alert']/div/div")
    AMAZON_LINK = (By.CSS_SELECTOR, "i[class='a-icon a-icon-logo']")

    def create_account_data(self, createAccountData):
        self.driver.find_element(*CreateAccountPage.NAME).send_keys(createAccountData["name"])
        self.driver.find_element(*CreateAccountPage.EMAIL).send_keys(createAccountData["email"])
        self.driver.find_element(*CreateAccountPage.PASSWORD).send_keys(createAccountData["pw"])
        self.driver.find_element(*CreateAccountPage.RE_ENTER_PASSWORD).send_keys(createAccountData["pwcheck"])
        self.driver.find_element(*CreateAccountPage.CREATE_ACCOUNT_BUTTON).click()

    def password_mismatch(self):
        return self.driver.find_element(*CreateAccountPage.PW_MISMATCH)

    def amazon_link(self):
        self.driver.find_element(*CreateAccountPage.AMAZON_LINK).click()
