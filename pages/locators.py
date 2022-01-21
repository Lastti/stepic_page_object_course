from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, '.login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '.register_form')
    EMAIL_FIELD = (By.NAME, 'registration-email')
    PASSWORD_FIELD = (By.NAME, 'registration-password1')
    RE_PASSWORD_FIELD = (By.NAME, 'registration-password2')
    REGISTER_SUBMIT = (By.NAME, 'registration_submit')


class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-add-to-basket')
    PRODUCT_ADDED_MESSAGE = (By.CSS_SELECTOR, '.alert-success strong')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    PRODUCT_PRICE_FROM_BASKET = (By.CSS_SELECTOR, '.alertinner p strong')
    PRODUCT_NAME = (By.CSS_SELECTOR, '.col-sm-6.product_main h1')
    PRODUCT_NAME_FROM_BASKET = (By.CSS_SELECTOR, '.alert-success:first-child .alertinner strong')


class BasketPageLocators():
    BASKET_PAGE = (By.CSS_SELECTOR, '.btn-group .btn-default:first-child')
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, '.col-sm-6.h3')
    EMPTY_BASKET_MESSAGE = (By.XPATH, '/html/body/div[2]/div/div[3]/div[2]/p')
