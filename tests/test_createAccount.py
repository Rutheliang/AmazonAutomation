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
        action.move_to_element(home_page.hover_signin()).perform()
        home_page.register_link()

        create_account = CreateAccountPage(self.driver)
        create_account.create_account_data(createAccountData)

        self.passwordMismatch = create_account.password_mismatch().text

        assert "Passwords must match" == self.passwordMismatch

        create_account.amazon_link()

        self.driver.refresh()

    @pytest.fixture(params=CreateAccountPageData.test_CreateAccountPage_Data )
    def createAccountData(self, request):
        return request.param


