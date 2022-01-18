from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to cart button is not presented"

    def should_be_succeed_message(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_ADDED_MESSAGE), \
            "There is no message that product successfully added to basket"

    def get_the_product_name(self):
        name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        return name.text

    def get_the_product_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        return price.text


    def should_be_expected_name_vol2(self, name):
        actual_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_BASKET)
        assert actual_name.text == name, \
            f'Product name from the basket: {actual_name.text} is not the same as actual product name: {name}'

    def should_be_expected_price_vol2(self, price):
        actual_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_FROM_BASKET)
        assert actual_price.text == price, \
            f'Price from the basket: {actual_price.text} is not the same as actual product price: {price}'


    def should_be_expected_name(self):
        actual_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_FROM_BASKET)
        expected_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME)
        assert actual_name.text == expected_name.text, \
            f'Product name from the basket: {actual_name.text} is not the same as actual product name: {expected_name.text}'


    def should_be_expected_price(self):
        actual_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_FROM_BASKET)
        expected_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        assert actual_price.text == expected_price.text, \
            f'Price from the basket: {actual_price.text} is not the same as actual product price: {expected_price.text}'
