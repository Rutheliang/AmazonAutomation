import pytest
from selenium.webdriver import ActionChains

from pageObject.CreateAccountPage import CreateAccountPage
from pageObject.HomePage import HomePage
from testData.CreateAccountPageData import CreateAccountPageData
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_createAccount(self, createAccountData):
        action = ActionChains(self.driver)
        home_page = HomePage(self.driver)
        action.move_to_element(home_page.getHover()).perform()
        home_page.getStart().click()

        account_page = CreateAccountPage(self.driver)
        account_page.getName().send_keys(createAccountData["name"])
        account_page.getEmail().send_keys(createAccountData["email"])
        account_page.getPassword().send_keys(createAccountData["pw"])
        account_page.getPwcheck().send_keys(createAccountData["pwcheck"])
        account_page.getButton3().click()
        self.passwordMismatch = account_page.getMismatch().text

        assert "Passwords must match" == self.passwordMismatch

        account_page.getAmazon().click()

        self.driver.refresh()

    @pytest.fixture(params=CreateAccountPageData.test_CreateAccountPage_Data )
    def createAccountData(self, request):
        return request.param


