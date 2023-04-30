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

    def user_name(self):
        return self.driver.find_element(*CreateAccountPage.NAME)

    def user_email(self):
        return self.driver.find_element(*CreateAccountPage.EMAIL)

    def user_password(self):
        return self.driver.find_element(*CreateAccountPage.PASSWORD)

    def re_enter_password(self):
        return self.driver.find_element(*CreateAccountPage.RE_ENTER_PASSWORD)

    def create_account_button(self):
        return self.driver.find_element(*CreateAccountPage.CREATE_ACCOUNT_BUTTON)

    def password_mismatch(self):
        return self.driver.find_element(*CreateAccountPage.PW_MISMATCH)

    def amazon_link(self):
        return self.driver.find_element(*CreateAccountPage.AMAZON_LINK)
