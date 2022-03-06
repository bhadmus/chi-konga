# pip install -r requirements.txt
class Login:
    """
    Element Locators for the login page
    """
    home_page = 'https://www.konga.com/'
    login_link = '[href="/account/login?return_url=/"]'
    email_field = '[name="username"]'
    password_field = '[name="password"]'
    login_button = '._0a08a_3czMG._988cf_1aDdJ'
    username1 = 'ademola.bhadmus@konga.com'
    password1 = 'Sanguine12@'
    username2 = 'chichianwuna@gmail.com'
    password2 = 'Di@mondg1rl'


class Cart:
    """
    Element Locators for the cart page
    """
    cart_button = '[class="_8486b_25fFV _16536_xxIKG"]>a[href="/cart/overview"]'
    cart_message = '._755e3_2hSjz>h3'


class Order:
    """
    Element Locators for the order page
    """
    account_button = '._12e27_1r3kc ._16536_xxIKG>span'
    order_button = "._12e27_1r3kc [href='\/account\/orders']"
    order_history_button = '._2e6a2_1gFdm.fb688_312WU'

