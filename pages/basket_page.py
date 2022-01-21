from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "URL does not contain login substring"

    def should_be_empty_basket_message(self):
        assert self.is_element_present(
            *BasketPageLocators.EMPTY_BASKET_MESSAGE), 'There is no message, basket is not empty'

    def should_no_have_products_in_basket(self):
        assert self.is_not_element_present(
            *BasketPageLocators.PRODUCTS_IN_BASKET), 'Basket is not enpty. There are products in it'
