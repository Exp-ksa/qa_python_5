from selenium import webdriver
from selenium.webdriver.chrome.options import Options # Chrome
from selenium.webdriver.firefox.options import Options as FirefoxOptions  # Firefox
import pytest

from url import REGISTER_URL, LOGIN_URL, FOGOT_URL 
from locators import Login_Locators
from data import Credentials


@pytest.fixture(scope="function")
def driver():
    options = Options()
    #options.add_argument("--window-size=1920,1080") #Запуск в разрешении 1920*1080
    options.add_argument('--start-maximized') 
    options.add_argument('--disable-popup-blocking')  # Отключить блокировку всплывающих окон
    #options.add_argument("--headless")  # Запуск в headless режиме, если нужно
    driver = webdriver.Chrome(options=options)

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def driver_firefox():
    options = FirefoxOptions()
    #options.add_argument("--window-size=1920,1080") #Запуск в разрешении 1920*1080
    options.add_argument('--start-maximized') 
    options.add_argument('--disable-popup-blocking')  # Отключить блокировку всплывающих окон
    #options.add_argument("--headless")  # Запуск в headless режиме, если нужно
    driver = webdriver.Firefox(options=options)

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def register_page(driver):
    driver.get(REGISTER_URL)
    return driver

@pytest.fixture(scope="function")
def main_page(driver):
    driver.get(LOGIN_URL)
    driver.find_element(*Login_Locators.EMAIL_FIELD).send_keys(Credentials.email)
    driver.find_element(*Login_Locators.PASSWORD_FIELD).send_keys(Credentials.password)
    driver.find_element(*Login_Locators.LOGIN_BUTTON).click()
    return driver

@pytest.fixture(scope="function")
def fogot_page(driver):
    driver.get(FOGOT_URL)
    return driver