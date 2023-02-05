from selenium.webdriver.common.by import By


class CreateAccountPage:

    def __init__(self, driver):
        self.driver = driver

    name = (By.ID, "ap_customer_name")
    email = (By.ID, "ap_email")
    password = (By.ID, "ap_password")
    pwcheck = (By.ID, "ap_password_check")
    button3 = (By.ID, "continue")
    mismatch = (By.XPATH, "//div[@id='auth-password-mismatch-alert']/div/div")
    amazon = (By.CSS_SELECTOR, "i[class='a-icon a-icon-logo']")

    def getName(self):
        return self.driver.find_element(*CreateAccountPage.name)

    def getEmail(self):
        return self.driver.find_element(*CreateAccountPage.email)

    def getPassword(self):
        return self.driver.find_element(*CreateAccountPage.password)

    def getPwcheck(self):
        return self.driver.find_element(*CreateAccountPage.pwcheck)

    def getButton3(self):
        return self.driver.find_element(*CreateAccountPage.button3)

    def getMismatch(self):
        return self.driver.find_element(*CreateAccountPage.mismatch)

    def getAmazon(self):
        return self.driver.find_element(*CreateAccountPage.amazon)
