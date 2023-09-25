

# from selenium.common import NoSuchElementException

from selenium.webdriver.support import expected_conditions
from Utilities.Readconfigfile import Readvalues
from PageObjects.loginpage import LoginPage
from Utilities.logger import LogGen


class TestLogin:
    username = Readvalues.getusername()
    password = Readvalues.getpassword()
    firstname = Readvalues.first_name()
    lastname = Readvalues.last_name()
    zipcode = Readvalues.zip_code()
    log = LogGen.loggen()
    url = Readvalues.url()

    def test_url_01(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.log.info('test_url_01 Opening Browser and URL')
        if self.driver.title == 'Swag Labs':
            self.log.info('test_url_01 checking page title')

            assert True
            self.log.info('test_url_01 is Passed')

        else:
            self.log.info('test_url_01 is Failed')
            self.driver.save_screenshot(
                "C:\\Users\\ajayj\\PycharmProjects\\demo_framework\\Screenshots\\test_url_01_FAIL.png")
            assert False
        self.log.info('test_url_01 is Completed')
        self.driver.close()

    def test_url_02(self, setup):

        self.driver = setup
        self.driver.get(self.url)
        self.log.info('test_url_02 Opening Browser and URL')

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.log.info('test_url_02 Insert Username ->' + self.username)

        self.lp.enter_password(self.password)
        self.log.info('test_url_02 Insert Password ->' + self.password)

        self.lp.click_login()
        self.log.info('test_url_02 Clicked Login')

        self.lp.wait.until(expected_conditions.presence_of_element_located(
            self.lp.Text_Menu_Button_XPATH))
        self.log.info('test_url_02 Verified Menu Button')

        if self.lp.login_status() is True:
            self.log.info('test_url_02 Checked Login Status')

            self.lp.click_menu_button()
            self.log.info('test_url_02 Clicked Menu Button')
            self.driver.implicitly_wait(4)

            self.lp.click_logout_button()
            self.log.info('test_url_02 Clicked Logout Button')

            self.driver.close()
            self.log.info('test_url_02 Is Passed')

            assert True

        else:
            self.log.info('test_url_02 Is Failed')
            self.driver.save_screenshot(
                "C:\\Users\\ajayj\\PycharmProjects\\demo_framework\\Screenshots\\test_url_02_FAIL.png")
            self.driver.close()
            assert False
        self.log.info('test_url_02 Is Completed')

    def test_order_03(self, setup):
        self.driver = setup
        self.driver.get(self.url)
        self.log.info('test_order_03 Opening Browser and URL')

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(self.username)
        self.log.info('test_order_03 Insert Username ->' + self.username)

        self.lp.enter_password(self.password)
        self.log.info('test_order_03 Insert Password ->' + self.password)

        self.lp.click_login()
        self.log.info('test_order_03 Clicked To Login')

        if self.lp.login_status() is True:
            self.log.info('test_order_03 Login Successful')

            pass
        else:
            self.log.info('test_order_03 Login Failed')

            self.driver.save_screenshot(
                "C:\\Users\\ajayj\\PycharmProjects\\demo_framework\\Screenshots\\test_order_01_login_status_FAIL.png")
            assert False
        self.lp.add_bike_light()
        self.log.info('test_order_03 Bike Light Added To Cart')

        self.lp.add_fleece_jacket()
        self.log.info('test_order_03 Fleece Jacket Added To Cart')

        self.lp.click_on_cart()
        self.log.info('test_order_03 Clicked To Cart')

        if self.lp.verify_page_checkout_button() is True:
            self.log.info('test_order_03 verified Checkout Button')

            pass
        else:
            self.log.info('test_order_03 Failed to verify Checkout Button')
            self.driver.save_screenshot(
                "C:\\Users\\ajayj\\PycharmProjects\\demo_framework\\Screenshots\\test_order_01_checkout_button_FAIL.png")
        self.lp.click_checkout_button()
        self.log.info('test_order_03 Clicked To Checkout Button')

        self.lp.enter_first_name(self.firstname)
        self.log.info('test_order_03 Entered First Name ->' + self.firstname)

        self.lp.enter_last_name(self.lastname)
        self.log.info('test_order_03 Entered Lastname Name ->' + self.lastname)

        self.lp.enter_zip_code(self.zipcode)
        self.log.info('test_order_03 Entered Zip Code ->' + self.zipcode)

        self.lp.click_checkout_continue()
        self.log.info('test_order_03 Clicked To Continue')

        self.lp.click_finish_button()
        self.log.info('test_order_03 Clicked To Finish Button')

        if self.lp.verify_placed_order() is True:
            self.log.info('test_order_03 Verified Placed Order')
            assert True
        else:
            self.log.info('test_order_03 Failed To Verify Placed Order')
            self.log.info('test_order_03 Entered First Name')

            self.driver.save_screenshot(
                "C:\\Users\\ajayj\\PycharmProjects\\demo_framework\\Screenshots\\test_order_01_finish_button_FAIL.png")
            assert False
        self.driver.close()
        self.log.info('test_order_03 Is Complete')

    def test_login_param_04(self, setup, getlogindata):

        self.driver = setup
        self.driver.get(self.url)
        self.log.info('test_login_param_04 Opening Browser and URL')

        self.lp = LoginPage(self.driver)
        self.lp.enter_username(getlogindata[0])
        self.log.info('test_login_param_04 Insert Username ->' + getlogindata[0])

        self.lp.enter_password(getlogindata[1])
        self.log.info('test_login_param_04 Insert Password ->' + getlogindata[1])

        self.lp.click_login()
        self.log.info('test_login_param_04 Clicked Login')
        self.driver.implicitly_wait(2)

        login_status = []

        if self.lp.login_status() is True:
            if getlogindata[2] == 'Pass':
                self.log.info('test_login_param_04 Verified Menu Button')

                login_status.append('Pass')
                self.log.info('test_login_param_04 Checked Login Status')

                self.lp.click_menu_button()
                self.log.info('test_login_param_04 Clicked Menu Button')
                self.driver.implicitly_wait(4)

                self.lp.click_logout_button()
                self.log.info('test_login_param_04 Clicked Logout Button')

                self.driver.close()
            elif getlogindata[2] == 'Fail':
                login_status.append('Fail')
                self.log.info('test_login_param_04 Checked Login Status')

                self.lp.click_menu_button()
                self.log.info('test_login_param_04 Clicked Menu Button')
                self.driver.implicitly_wait(4)

                self.lp.click_logout_button()
                self.log.info('test_login_param_04 Clicked Logout Button')

                self.driver.close()

        else:
            if getlogindata[2] == 'Fail':
                login_status.append('Pass')
                self.driver.save_screenshot(
                    "C:\\Users\\ajayj\\PycharmProjects\\demo_framework\\Screenshots\\test_login_param_04_Fail.png")
                self.driver.close()
            elif getlogindata[2] == 'Pass':
                login_status.append('Fail')

                self.driver.save_screenshot(
                    "C:\\Users\\ajayj\\PycharmProjects\\demo_framework\\Screenshots\\test_login_param_04_FAIL.png")
                self.driver.close()
            self.log.info('test_login_param_04 Is Completed')
        if 'Fail' not in login_status:
            self.log.info('test_login_param_04 Is Passed')
            assert True
        else:
            self.log.info('test_login_param_04 Is Failed')
            assert False
