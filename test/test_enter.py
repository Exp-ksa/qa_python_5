from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..locators import Registration_Locators, Login_Locators, Forgot_Locators, Main_Locators
from ..data import Credentials


class TestEnter:

    def test_login_via_enter_account_button_on_home_page(self, main_page):

        driver = main_page 
        driver.find_element(*Main_Locators.LOGIN_ACCAUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_BUTTON))

        assert "login" in driver.current_url

        email_field = driver.find_element(*Login_Locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(Credentials.email)

        password_field = driver.find_element(*Login_Locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(Credentials.password)

        driver.find_element(*Login_Locators.LOGIN_BUTTON).click()

        button_order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))

        assert button_order.text == 'Оформить заказ'

    def test_login_by_profile_button_on_main_page(self, main_page):
        
        driver = main_page 
        driver.find_element(*Main_Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_BUTTON))

        assert "login" in driver.current_url

        email_field = driver.find_element(*Login_Locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(Credentials.email)

        password_field = driver.find_element(*Login_Locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(Credentials.password)

        driver.find_element(*Login_Locators.LOGIN_BUTTON).click()

        button_order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))

        assert button_order.text == 'Оформить заказ'

    def test_login_by_button_on_registration_form(self, register_page):

        driver = register_page
        driver.find_element(*Registration_Locators.LINK_LOGIN).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_BUTTON))

        assert "login" in driver.current_url

        email_field = driver.find_element(*Login_Locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(Credentials.email)

        password_field = driver.find_element(*Login_Locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(Credentials.password)

        driver.find_element(*Login_Locators.LOGIN_BUTTON).click()

        button_order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))

        assert button_order.text == 'Оформить заказ'
    
    def test_login_by_button_on_forgot_password_form(self, forgot_page):

        driver = forgot_page
        driver.find_element(*Forgot_Locators.LINK_LOGIN).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_BUTTON))

        assert "login" in driver.current_url

        email_field = driver.find_element(*Login_Locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(Credentials.email)

        password_field = driver.find_element(*Login_Locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(Credentials.password)

        driver.find_element(*Login_Locators.LOGIN_BUTTON).click()

        button_order = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))

        assert button_order.text == 'Оформить заказ'