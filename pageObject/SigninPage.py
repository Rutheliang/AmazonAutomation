from selenium.webdriver.common.by import By


class SigninPage:

    def __init__(self, driver):
        self.driver = driver

    signin = (By.ID, "ap_email")
    button = (By.CSS_SELECTOR, ".a-button-input")
    pw = (By.ID, "ap_password")
    button2 = (By.ID, "signInSubmit")
    amazon = (By.CSS_SELECTOR, "i[class='a-icon a-icon-logo']")

    def getSignin(self):
        return self.driver.find_element(*SigninPage.signin)
        # self.driver.find_element(By.ID, "ap_email").send_keys("test@aol.com")

    def getButton(self):
        return self.driver.find_element(*SigninPage.button)
        # self.driver.find_element(By.CSS_SELECTOR, ".a-button-input").click()

    def getPw(self):
        return self.driver.find_element(*SigninPage.pw)
        # self.driver.find_element(By.ID, "ap_password").send_keys("Test@123")

    def getButton2(self):
        return self.driver.find_element(*SigninPage.button2)
        # self.driver.find_element(By.ID, "signInSubmit").click()

    def getAmazon(self):
        return self.driver.find_element(*SigninPage.amazon)
