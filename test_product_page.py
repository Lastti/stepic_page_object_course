import time

from .pages import product_page
from .pages.product_page import ProductPage
from .pages.locators import ProductPageLocators
from selenium.webdriver.common.by import By

def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    time.sleep(3000)
    page.should_be_expected_name()
    page.should_be_expected_price()

