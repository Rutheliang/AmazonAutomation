from selenium.webdriver.common.by import By


class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver

    NAME = (By.ID, "ap_customer_name")
    EMAIL = (By.ID, "ap_email")
    PASSWORD = (By.ID, "ap_password")
    PWCHECK = (By.ID, "ap_password_check")
    BUTTON3 = (By.ID, "continue")
    MISMATCH = (By.XPATH, "//div[@id='auth-password-mismatch-alert']/div/div")
    AMAZON = (By.CSS_SELECTOR, "i[class='a-icon a-icon-logo']")

    def getName(self):
        return self.driver.find_element(*CreateAccountPage.NAME)

    def getEmail(self):
        return self.driver.find_element(*CreateAccountPage.EMAIL)

    def getPassword(self):
        return self.driver.find_element(*CreateAccountPage.PASSWORD)

    def getPwcheck(self):
        return self.driver.find_element(*CreateAccountPage.PWCHECK)

    def getButton3(self):
        return self.driver.find_element(*CreateAccountPage.BUTTON3)

    def getMismatch(self):
        return self.driver.find_element(*CreateAccountPage.MISMATCH)

    def getAmazon(self):
        return self.driver.find_element(*CreateAccountPage.AMAZON)
