from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Login_Locators, Main_Locators, Profile_Locators
from data import Credentials

class TestExit:
    def test_logout_by_exit_button_in_profile(self, login_page):

        driver = login_page
        
        email_field = driver.find_element(*Login_Locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(Credentials.email)

        password_field = driver.find_element(*Login_Locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(Credentials.password)

        driver.find_element(*Login_Locators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.ORDER_BUTTON))

        driver.find_element(*Main_Locators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Profile_Locators.EXIT_BUTTON))

        driver.find_element(*Profile_Locators.EXIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_BUTTON))

        assert "login" in driver.current_url 
