from selenium.webdriver.common.by import By


class ResultPage:

    def __init__(self, driver):
        self.driver = driver

    brand = (By.XPATH, "//li[@aria-label='Roblox']/span/a/div")
    age = (By.XPATH, "//li[@aria-label='5 to 7 Years']/span/a/div")
    choose = (By.XPATH, "//div//div[4]//div//div//div//div//div[2]//div//h2//a//span")

    def getBrand(self):
        return self.driver.find_element(*ResultPage.brand)
        # self.driver.find_element(By.XPATH, "//li[@aria-label='Roblox']/span/a/div")

    def getAge(self):
        return self.driver.find_element(*ResultPage.age)
        # self.driver.find_element(By.XPATH, "//li[@aria-label='5 to 7 Years']/span/a/div")

    def getChoose(self):
        return self.driver.find_element(*ResultPage.choose)
        # self.driver.find_element(By.XPATH, "//div//div[3]//div//div//div//div//div[2]//div//h2//a//span").click()
