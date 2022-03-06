from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from element_mapper.element_mapper import Login, Cart, Order


class Konga:
    """
    All actions to automate test scenarios on the Konga site
    """
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 15)
        Login()
        Cart()

    def open_site(self):
        self.driver.get(Login.home_page)
        self.driver.maximize_window()

    def click_any_element(self, element):
        self.driver.find_element(By.CSS_SELECTOR, element).click()

    def type_any_text(self, field, text):
        self.driver.find_element(By.CSS_SELECTOR, field).send_keys(text)

    def wait_for_visibility(self, element):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, element)))

    def wait_to_be_clickable(self, element):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))

    def login(self, username, password):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Login.login_link)))
        self.driver.find_element(By.CSS_SELECTOR, Login.login_link).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Login.email_field)))
        self.driver.find_element(By.CSS_SELECTOR, Login.email_field).send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, Login.password_field).send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, Login.login_button).click()

    def check_cart(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Cart.cart_button)))
        self.driver.find_element(By.CSS_SELECTOR, Cart.cart_button).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Cart.cart_message)))
        try:
            texts = self.driver.find_element(By.CSS_SELECTOR, Cart.cart_message).text
            assert texts == "Your cart is empty."
            print('Text Found')
        except:
            raise AssertionError('Text Not Found')

    def order_history(self):
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, Order.account_button)))
        self.driver.find_element(By.CSS_SELECTOR, Order.account_button).click()
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Order.order_button)))
        self.driver.find_element(By.CSS_SELECTOR, Order.order_button).click()
        try:
            self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, Order.order_history_button)))
            texts = self.driver.find_element(By.CSS_SELECTOR, Order.order_history_button).text
            assert texts == "Order History"
            print('Text Found')
        except:
            raise AssertionError('Text Not Found')

    def close_site(self):
        self.driver.quit()
