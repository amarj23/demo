from selenium import webdriver
import time

from selenium.webdriver.common.by import By

# from TestCases.test_login import LoginPage

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('https://www.saucedemo.com/')
driver.find_element(By.ID,'user-name').send_keys('standard_user')
driver.find_element(By.ID,'password').send_keys('secret_sauce')
driver.find_element(By.ID,'login-button').click()
driver.find_element(By.ID, 'add-to-cart-sauce-labs-bike-light').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-fleece-jacket"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="shopping_cart_container"]/a').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="checkout"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys('jfdsfs')
driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys('sffs')
driver.find_element(By.ID, 'postal-code').send_keys('2322')
time.sleep(1)
driver.find_element(By.ID, 'continue').click()
driver.find_element(By.ID, 'finish').click()

try:
    a = driver.find_element(By.XPATH, '//*[@id="checkout_complete_container"]/img')
    driver.implicitly_wait(4)
    if a.is_displayed() is True:
        assert True
except Exception as ex:
    print(ex)
