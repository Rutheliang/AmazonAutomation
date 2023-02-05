
import pytest

from pageObject.CartCheckoutPage import CartCheckoutPage
from pageObject.HomePage import HomePage
from pageObject.ResultPage import ResultPage
from pageObject.SigninPage import SigninPage
from testData.SigninPageData import SigninPageData
from utilities.BaseClass import BaseClass

import time


class TestOne(BaseClass):

    def test_searchItem(self, signinData):
        log = self.getLogger()
        homePage = HomePage(self.driver)

        log.info("Search roblox item")
        homePage.getSearch().send_keys("roblox")

        time.sleep(2)

        log.info("Select roblox plushies")
        roblox = homePage.getItems()
        log.info(len(roblox))
        for robloxP in roblox:
            if robloxP.text == "roblox plushies":
                robloxP.click()
                break

        log.info(homePage.getValue().get_attribute("value"))

        resultPage = ResultPage(self.driver)
        resultPage.getBrand().click()
        resultPage.getAge().click()
        resultPage.getChoose().click()

        log.info("Add selected item to cart")
        cartCheckoutPage = CartCheckoutPage(self.driver)
        cartCheckoutPage.getCart().click()
        cartCheckoutPage.getCheckout().click()

        signInPage = SigninPage(self.driver)
        signInPage.getSignin().send_keys(signinData["email"])

        signInPage.getButton().click()
        signInPage.getPw().send_keys(signinData["password"])
        signInPage.getButton2().click()

        self.driver.refresh()

        signInPage.getAmazon().click()

    @pytest.fixture(params=SigninPageData.test_SignPage_Data)
    def signinData(self, request):
        return request.param

