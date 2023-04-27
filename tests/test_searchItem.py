
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
        home_page = HomePage(self.driver)

        log.info("Search roblox item")
        home_page.getSearch().send_keys("roblox plushies")

        time.sleep(2)

        log.info("Select roblox plushies")
        roblox = home_page.getItems()
        log.info(len(roblox))
        for item in roblox:
            if item.text == "roblox plushies for girls":
                item.click()
                break

        log.info(home_page.getValue().get_attribute("value"))

        result_page = ResultPage(self.driver)
        result_page.add_selected_item_to_cart()

        log.info("Selected item added to cart")
        cart_checkout_page = CartCheckoutPage(self.driver)
        cart_checkout_page.getCart().click()
        cart_checkout_page.getCheckout().click()

        signin_page = SigninPage(self.driver)
        signin_page.getSignin().send_keys(signinData["email"])

        signin_page.getButton().click()
        signin_page.getPw().send_keys(signinData["password"])
        signin_page.getButton2().click()

        self.driver.refresh()

        signin_page.getAmazon().click()

    @pytest.fixture(params=SigninPageData.test_SignPage_Data)
    def signinData(self, request):
        return request.param

