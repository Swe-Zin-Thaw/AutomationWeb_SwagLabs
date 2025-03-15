from selenium import webdriver
from selenium.webdriver.common.by import By
import re
import time

#Locator
USER_NAME = "user-name"
PASSWORD = "password"
LOGIN_BUTTON = "login-button"
ERROR_MSG = "/html/body/div/div/div[2]/div[1]/div/div/form/div[3]/h3"
EXPECTED_URL_HOME = "https://www.saucedemo.com/inventory.html"
SORT = "product_sort_container"
NAME_Z_TO_A = "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[2]"
NAME_A_TO_Z = "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[1]"
PRICE_LOW_TO_HIGH = "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[3]"
PRICE_HIGH_TO_LOW = "/html/body/div/div/div/div[1]/div[2]/div/span/select/option[4]"
ADD_TSHIRT_BLACK = "add-to-cart-sauce-labs-bolt-t-shirt"
ADD_TSHIRT_RED = "add-to-cart-test.allthethings()-t-shirt-(red)"
ADD_BIKE_LIGHT = "add-to-cart-sauce-labs-bike-light"
CART = "shopping_cart_link"
EXPECTED_URL_CART = "https://www.saucedemo.com/cart.html"
REMOVE_TSHIRT_BLACK = "remove-sauce-labs-bolt-t-shirt"
CONTINUE_SHOPPING = "continue-shopping"
CHECK_OUT = "checkout"
EXPECTED_URL_CHECK_OUT = "https://www.saucedemo.com/checkout-step-one.html"
CANCEL = "cancel"
CONTINUE = "continue"
FIRST_NAME = "first-name"
LAST_NAME = "last-name"
POSTAL_CODE = "postal-code"
ERROR_MSG2 = "/html/body/div/div/div/div[2]/div/form/div[1]/div[4]"
EXPECTED_URL_CHECK_OUT_2 = "https://www.saucedemo.com/checkout-step-two.html"
PAYMENT_INFO = "/html/body/div/div/div/div[2]/div/div[2]/div[2]"
SHIPPING_INFO = "/html/body/div/div/div/div[2]/div/div[2]/div[4]"
PRICE_INFO_SUBTOTAL = "summary_subtotal_label"
PRICE_INFO_TAX = "summary_tax_label"
PRICE_INFO_TOTAL = "summary_total_label"
FINISH = "finish"
CHECKOUT_COMPLETE = "/html/body/div/div/div/div[1]/div[2]/span"
THANK_YOU = "/html/body/div/div/div/div[2]/h2"
BACK_HOME = "back-to-products"
MENU = "react-burger-menu-btn"
ABOUT_SIDEBAR_LINK = "about_sidebar_link"
LOGOUT_SIDEBAR_LINK = "logout_sidebar_link"
EXPECTED_URL_ABOUT = "https://saucelabs.com/"


class TestSwagLab:

    driver = webdriver.Firefox()

    def test_open_browser(self):
        print("------------------Opening Browser--------------")
        time.sleep(3)
        self.driver.get("https://www.saucedemo.com/")
        time.sleep(3)
        self.driver.maximize_window()
        time.sleep(3)
        print("Navigate to SauceLab Website")

    def test_login(self):
        print("------------------Login Validation Checking----------------")
        self.driver.find_element(By.ID, LOGIN_BUTTON).click()
        error_msg = self.driver.find_element(By.XPATH, ERROR_MSG).text
        print("Empty username and password information: ", error_msg)
        time.sleep(3)
        self.driver.find_element(By.ID, USER_NAME).send_keys("standard_user")
        self.driver.find_element(By.ID, LOGIN_BUTTON).click()
        error_msg = self.driver.find_element(By.XPATH, ERROR_MSG).text
        print("Empty password information: ", error_msg)
        time.sleep(3)
        self.driver.find_element(By.ID, USER_NAME).clear()
        self.driver.find_element(By.ID, PASSWORD).send_keys("secret_sauce")
        self.driver.find_element(By.ID, LOGIN_BUTTON).click()
        error_msg = self.driver.find_element(By.XPATH, ERROR_MSG).text
        print("Empty username information: ", error_msg)
        time.sleep(3)
        self.driver.find_element(By.ID, USER_NAME).send_keys("swezinthaw")
        self.driver.find_element(By.ID, LOGIN_BUTTON).click()
        error_msg = self.driver.find_element(By.XPATH, ERROR_MSG).text
        print("Incorrect username or password: ", error_msg)
        time.sleep(3)
        self.driver.find_element(By.ID, USER_NAME).clear()
        self.driver.find_element(By.ID, USER_NAME).send_keys("standard_user")
        self.driver.find_element(By.ID, LOGIN_BUTTON).click()

    def test_verify_login(self):
        print("------------------Verify Login Status----------------")
        actual_url = self.driver.current_url
        assert EXPECTED_URL_HOME == actual_url
        print("Login Successful!")
        time.sleep(3)

    def test_sort_list(self):
        print("------------------Sorting List----------------")
        self.driver.find_element(By.CLASS_NAME, SORT).click()
        self.driver.find_element(By.XPATH, NAME_Z_TO_A).click()
        print("Sorting Name Z to A")
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, SORT).click()
        self.driver.find_element(By.XPATH, PRICE_LOW_TO_HIGH).click()
        print("Sorting Price Low To High")
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, SORT).click()
        self.driver.find_element(By.XPATH, PRICE_HIGH_TO_LOW).click()
        print("Sorting Price High to Low")
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, SORT).click()
        self.driver.find_element(By.XPATH, NAME_A_TO_Z).click()
        print("Sorting Name A to Z")
        time.sleep(3)

    def test_about_page_menu(self):
        print("------------------About the Page Menu----------------")
        self.driver.find_element(By.ID, MENU).click()
        self.driver.find_element(By.ID, ABOUT_SIDEBAR_LINK).click()
        time.sleep(3)
        actual_url = self.driver.current_url
        assert EXPECTED_URL_ABOUT == actual_url
        print("Navigate to About Page!")
        time.sleep(3)
        self.driver.back()
        time.sleep(3)

    def test_add_to_cart(self):
        print("------------------Add Item to Cart-----------------")
        self.driver.find_element(By.ID, ADD_TSHIRT_BLACK).click()
        print("Adding item 1 to cart")
        time.sleep(3)
        self.driver.find_element(By.ID, ADD_TSHIRT_RED).click()
        print("Adding item 2 to cart")
        time.sleep(3)
        self.driver.find_element(By.ID, ADD_BIKE_LIGHT).click()
        print("Adding item 3 to cart")
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, CART).click()

    def test_verify_cart(self):
        print("------------------Verify Cart Page----------------")
        actual_url = self.driver.current_url
        assert EXPECTED_URL_CART == actual_url
        print("Navigate to Swag Lab Cart Page!")
        time.sleep(3)

    def test_remove_from_cart(self):
        print("------------------Remove Item from Cart----------------")
        self.driver.find_element(By.ID, REMOVE_TSHIRT_BLACK).click()
        print("Removing item 1 from cart")
        time.sleep(3)
        self.driver.find_element(By.ID, CONTINUE_SHOPPING).click()
        print("Back to home page!")
        self.driver.find_element(By.ID, ADD_TSHIRT_BLACK).click()
        print("Adding again item 1 to cart")
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, CART).click()
        self.driver.find_element(By.ID, CHECK_OUT).click()

    def test_checkout(self):
        print("------------------Checkout Page----------------")
        actual_url = self.driver.current_url
        assert EXPECTED_URL_CHECK_OUT == actual_url
        print("Navigate to Check Out Page!")
        time.sleep(3)
        self.driver.find_element(By.ID, CANCEL).click()
        print("Back to Cart Page!")
        print("------------------Check Out Validation Checking----------------")
        self.driver.find_element(By.ID, CHECK_OUT).click()
        self.driver.find_element(By.ID, CONTINUE).click()
        error_msg = self.driver.find_element(By.XPATH, ERROR_MSG2).text
        print("Empty information: ", error_msg)
        time.sleep(3)
        self.driver.find_element(By.ID, LAST_NAME).send_keys("Thaw")
        self.driver.find_element(By.ID, POSTAL_CODE).send_keys("111111")
        self.driver.find_element(By.ID, CONTINUE).click()
        error_msg = self.driver.find_element(By.XPATH, ERROR_MSG2).text
        print("Empty FirstName information: ", error_msg)
        time.sleep(3)
        self.driver.find_element(By.ID, FIRST_NAME).send_keys("Swe Zin")
        self.driver.find_element(By.ID, LAST_NAME).clear()
        self.driver.find_element(By.ID, CONTINUE).click()
        error_msg = self.driver.find_element(By.XPATH, ERROR_MSG2).text
        print("Empty LastName information: ", error_msg)
        time.sleep(3)
        self.driver.find_element(By.ID, POSTAL_CODE).clear()
        self.driver.find_element(By.ID, LAST_NAME).send_keys("Thaw")
        self.driver.find_element(By.ID, CONTINUE).click()
        error_msg = self.driver.find_element(By.XPATH, ERROR_MSG2).text
        print("Empty Postal Code Information: ", error_msg)
        time.sleep(3)
        self.driver.find_element(By.ID, POSTAL_CODE).send_keys("111111")
        self.driver.find_element(By.ID, CONTINUE).click()

    def test_checkout_step2(self):
        print("------------------Checkout Step 2----------------")
        time.sleep(3)
        actual_url = self.driver.current_url
        assert EXPECTED_URL_CHECK_OUT_2 == actual_url
        print("Navigate to Check Out Step 2 Page!")

    def test_payment_information(self):
        print("------------------Payment Information----------------")
        payment = self.driver.find_element(By.XPATH,PAYMENT_INFO).text
        print("Payment Information: ", payment)
        time.sleep(3)
        shipping = self.driver.find_element(By.XPATH, SHIPPING_INFO).text
        print("Shipping Information: ", shipping)
        time.sleep(3)
        price_sub_total = self.driver.find_element(By.CLASS_NAME, PRICE_INFO_SUBTOTAL).text
        price_tax = self.driver.find_element(By.CLASS_NAME, PRICE_INFO_TAX).text
        price_total = self.driver.find_element(By.CLASS_NAME, PRICE_INFO_TOTAL).text
        # Remove non-numeric characters except "."
        price_sub_total = float(re.sub(r"[^\d.]", "", price_sub_total))
        price_tax = float(re.sub(r"[^\d.]", "", price_tax))
        price_total = float(re.sub(r"[^\d.]", "", price_total))
        price_total = float(price_total)
        #Check total price
        total = price_sub_total + price_tax
        assert total == price_total
        print(f"Payment Information:\nItem total: ${price_sub_total:.2f}\nTax: ${price_tax:.2f}\nTotal: ${price_total:.2f}")

    def test_checkout_step3(self):
        print("------------------Checkout Step 3----------------")
        self.driver.find_element(By.ID, FINISH).click()
        print(self.driver.find_element(By.XPATH, CHECKOUT_COMPLETE).text)
        time.sleep(3)
        print(self.driver.find_element(By.XPATH, THANK_YOU).text)
        time.sleep(3)
        self.driver.find_element(By.ID, BACK_HOME).click()
        print("Navigate to Home Page!")

    def test_logout(self):
        print("------------------Logout-----------------")
        self.driver.find_element(By.ID, MENU).click()
        time.sleep(3)
        self.driver.find_element(By.ID, LOGOUT_SIDEBAR_LINK).click()
        time.sleep(3)
        print("Logout Successfully!")

#pytest SwagLabReport.py --html=report.html