
import pytest

from pageObject.CartCheckoutPage import CartCheckoutPage
from pageObject.HomePage import HomePage
from pageObject.SearchItemPage import SearchItemPage
from pageObject.SigninPage import SigninPage
from testData.SigninPageData import SigninPageData
from utilities.BaseClass import BaseClass
import time


class TestOne(BaseClass):

    def test_searchItem(self, signinData):
        log = self.getLogger()
        home_page = HomePage(self.driver)

        log.info("Search roblox item")
        home_page.search_item()

        time.sleep(2)

        log.info("Select roblox toys")
        roblox = home_page.get_items()
        log.info(len(roblox))
        for item in roblox:
            if item.text == "roblox toys":
                item.click()
                break

        log.info(home_page.item_selected().get_attribute("value"))

        result_page = SearchItemPage(self.driver)
        result_page.add_selected_item_to_cart()

        log.info("Item added to cart")
        cart_checkout_page = CartCheckoutPage(self.driver)
        cart_checkout_page.go_to_checkout()

        signin_page = SigninPage(self.driver)
        signin_page.user_signin(signinData)

        self.driver.refresh()

    @pytest.fixture(params=SigninPageData.test_SignPage_Data)
    def signinData(self, request):
        return request.param

