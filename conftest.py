from selenium import webdriver
from selenium.webdriver.chrome.options import Options # Chrome
import pytest

from url import REGISTER_URL, LOGIN_URL, FORGOT_URL, MAIN_URL 


@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.add_argument('--start-maximized') 
    options.add_argument('--disable-popup-blocking')  # Отключить блокировку всплывающих окон
    driver = webdriver.Chrome(options=options)

    driver.implicitly_wait(5)
    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def register_page(driver):
    driver.get(REGISTER_URL)
    return driver

@pytest.fixture(scope="function")
def login_page(driver):
    driver.get(LOGIN_URL)
    return driver

@pytest.fixture(scope="function")
def forgot_page(driver):
    driver.get(FORGOT_URL)
    return driver

@pytest.fixture(scope="function")
def main_page(driver):
    driver.get(MAIN_URL)
    return driver