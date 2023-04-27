from selenium.webdriver.common.by import By


class SigninPage:

    def __init__(self, driver):
        self.driver = driver

    SIGNIN = (By.ID, "ap_email")
    BUTTON = (By.CSS_SELECTOR, ".a-button-input")
    PW = (By.ID, "ap_password")
    BUTTON2 = (By.ID, "signInSubmit")
    AMAZON = (By.CSS_SELECTOR, "i[class='a-icon a-icon-logo']")

    def getSignin(self):
        return self.driver.find_element(*SigninPage.SIGNIN)
        # self.driver.find_element(By.ID, "ap_email").send_keys("test@aol.com")

    def getButton(self):
        return self.driver.find_element(*SigninPage.BUTTON)
        # self.driver.find_element(By.CSS_SELECTOR, ".a-button-input").click()

    def getPw(self):
        return self.driver.find_element(*SigninPage.PW)
        # self.driver.find_element(By.ID, "ap_password").send_keys("Test@123")

    def getButton2(self):
        return self.driver.find_element(*SigninPage.BUTTON2)
        # self.driver.find_element(By.ID, "signInSubmit").click()

    def getAmazon(self):
        return self.driver.find_element(*SigninPage.AMAZON)
