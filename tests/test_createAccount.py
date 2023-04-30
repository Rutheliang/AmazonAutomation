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
        create_account.user_name().send_keys(createAccountData["name"])
        create_account.user_email().send_keys(createAccountData["email"])
        create_account.user_password().send_keys(createAccountData["pw"])
        create_account.re_enter_password().send_keys(createAccountData["pwcheck"])
        create_account.create_account_button().click()
        self.passwordMismatch = create_account.password_mismatch().text

        assert "Passwords must match" == self.passwordMismatch

        create_account.amazon_link().click()

        self.driver.refresh()

    @pytest.fixture(params=CreateAccountPageData.test_CreateAccountPage_Data )
    def createAccountData(self, request):
        return request.param


