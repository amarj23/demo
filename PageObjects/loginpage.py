from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:

    Text_Username_ID = (By.ID, 'user-name')
    Text_Password_ID = (By.ID, 'password')
    Text_Login_Button_ID = (By.ID, 'login-button')
    Text_Menu_Button_XPATH = (By.XPATH, '//*[@id="react-burger-menu-btn"]')
    Text_Logout_Button_ID = (By.ID, 'logout_sidebar_link')

    Text_Bike_Light_Id = (By.ID, 'add-to-cart-sauce-labs-bike-light')
    Text_Fleece_Jacket_Xpath = (By.XPATH, '//*[@id="add-to-cart-sauce-labs-fleece-jacket"]')
    Text_Cart_Id = (By.ID, 'shopping_cart_container')
    Text_Checkout_Button_Id = (By.ID, "checkout")
    Text_Checkout_Firstname = (By.XPATH, '//*[@id="first-name"]')
    Text_Checkout_Lastname = (By.XPATH, '//*[@id="last-name"]')
    Text_Checkout_Zipcode = (By.ID, 'postal-code')
    Text_Checkout_Continue = (By.ID, 'continue')
    Text_Checkout_finish = (By.ID, 'finish')
    Test_Verify_Order_Complete = (By.XPATH, '//*[@id="checkout_complete_container"]/img')

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def enter_username(self, username):
        self.driver.find_element(*LoginPage.Text_Username_ID).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.Text_Password_ID).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPage.Text_Login_Button_ID).click()

    def click_menu_button(self):
        self.driver.find_element(*LoginPage.Text_Menu_Button_XPATH).click()

    def click_logout_button(self):
        self.driver.find_element(*LoginPage.Text_Logout_Button_ID).click()

    def login_status(self):

        try:
            self.driver.find_element(*LoginPage.Text_Menu_Button_XPATH)
            return True
        except NoSuchElementException as Ec:
            return False

    def add_bike_light(self):
        self.driver.find_element(*LoginPage.Text_Bike_Light_Id).click()

    def add_fleece_jacket(self):
        self.driver.find_element(*LoginPage.Text_Fleece_Jacket_Xpath).click()

    def click_on_cart(self):
        self.driver.find_element(*LoginPage.Text_Cart_Id).click()

    def verify_page_checkout_button(self):
        try:
            self.driver.find_element(*LoginPage.Text_Checkout_Button_Id)
            return True
        except Exception as checkout_button_ex:
            print('this exception is occurred during verify checkout button =>' + str(checkout_button_ex))
            return False

    def click_checkout_button(self):
        self.driver.find_element(*LoginPage.Text_Checkout_Button_Id).click()

    def enter_first_name(self, firstname):
        self.driver.find_element(*LoginPage.Text_Checkout_Firstname).send_keys(firstname)

    def enter_last_name(self, lastname):
        self.driver.find_element(*LoginPage.Text_Checkout_Lastname).send_keys(lastname)

    def enter_zip_code(self, zipcode):
        self.driver.find_element(*LoginPage.Text_Checkout_Zipcode).send_keys(zipcode)

    def click_checkout_continue(self):
        self.driver.find_element(*LoginPage.Text_Checkout_Continue).click()

    def click_finish_button(self):
        self.driver.find_element(*LoginPage.Text_Checkout_finish).click()

    def verify_placed_order(self):
        try:
            self.driver.find_element(*LoginPage.Test_Verify_Order_Complete)
            return True
        except Exception as ec:
            print('this exception is occurred during verify checkout button =>' + str(ec))



