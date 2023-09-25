

from selenium import webdriver
import pytest


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    else:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument('--headless')
        driver = webdriver.Chrome(options=chrome_option)
    return driver


@pytest.fixture(params=[
        ('standard_user', 'secret_sauce', 'Pass'),
        ('standard_dom', 'secret_sauce', 'Fail'),
        ('standard_user', 'beauty', 'Fail'),
        ('john', 'cena', 'Fail')])
def getlogindata(request):
    return request.param
