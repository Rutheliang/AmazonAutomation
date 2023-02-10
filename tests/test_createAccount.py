import pytest
from selenium.webdriver import ActionChains

from pageObject.CreateAccountPage import CreateAccountPage
from pageObject.HomePage import HomePage
from testData.CreateAccountPageData import CreateAccountPageData
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_createAccount(self, createAccountData):
        action = ActionChains(self.driver)
        homePage = HomePage(self.driver)
        action.move_to_element(homePage.getHover()).perform()
        homePage.getStart().click()

        accountPage = CreateAccountPage(self.driver)
        accountPage.getName().send_keys(createAccountData["name"])
        accountPage.getEmail().send_keys(createAccountData["email"])
        accountPage.getPassword().send_keys(createAccountData["pw"])
        accountPage.getPwcheck().send_keys(createAccountData["pwcheck"])
        accountPage.getButton3().click()
        self.passwordMismatch = accountPage.getMismatch().text

        assert "Passwords must match" == self.passwordMismatch

        accountPage.getAmazon().click()

        self.driver.refresh()

    @pytest.fixture(params=CreateAccountPageData.test_CreateAccountPage_Data )
    def createAccountData(self, request):
        return request.param


