import time
import pytest

from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage

class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope='function', autouse=True) #запуск каждую функцию внутри класса, автоматически без явного вызова
    def setup(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        email = str(time.time()) + "@fakemail.org"
        password = str(time.time())
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
        page = ProductPage(browser, link)
        page.open()
        page.should_be_add_to_cart_button()
        page.add_to_basket()
        price = page.get_the_product_price()
        page.should_be_expected_price_vol2(price)
        name = page.get_the_product_name()
        page.should_be_expected_name_vol2(name)

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

# link_list = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#              pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
#                           marks=pytest.mark.xfail),
#              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#              "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]
#
#
# @pytest.mark.parametrize('link', link_list)
def test_guest_can_add_product_to_basket(browser):
    # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    # time.sleep(300)
    price = page.get_the_product_price()
    page.should_be_expected_price_vol2(price)
    name = page.get_the_product_name()
    page.should_be_expected_name_vol2(name)

def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = LoginPage(browser, link)
    page.open()
    page.go_to_login_page()
    page.should_be_login_page()

def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_no_have_products_in_basket()
    basket_page.should_be_empty_basket_message()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_basket()
    page.should_dissappear()

@pytest.mark.xfail
def test_should_not_be_succeed_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

