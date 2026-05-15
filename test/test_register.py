from generate_credentials import generate_random_credentials
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Registration_Locators, Login_Locators

class TestRegister:
    def test_register(self, register_page):
        
        name, email, password = generate_random_credentials()
        
        driver = register_page
        driver.find_element(*Registration_Locators.NAME_FIELD).send_keys(name)
        driver.find_element(*Registration_Locators.EMAIL_FIELD).send_keys(email)
        driver.find_element(*Registration_Locators.PASSWORD_FIELD).send_keys(password)
        driver.find_element(*Registration_Locators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_BUTTON))
        login = driver.find_element(*Login_Locators.LOGIN_BUTTON).text

        assert login == 'Войти'

    def test_register_incorrect_password_with_one_symbol(self, register_page):
        
        name, email, _ = generate_random_credentials()
        short_password = 'a'

        driver = register_page
        name_field = driver.find_element(*Registration_Locators.NAME_FIELD)
        name_field.clear()
        name_field.send_keys(name)
    
        email_field = driver.find_element(*Registration_Locators.EMAIL_FIELD)
        email_field.clear()
        email_field.send_keys(email)
    
        password_field = driver.find_element(*Registration_Locators.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(short_password)

        driver.find_element(*Registration_Locators.REGISTER_BUTTON).click()
        
        error_message = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Registration_Locators.INCORRECT_PASSWORD))
        
        assert error_message.text == 'Некорректный пароль'
        assert "register" in driver.current_url
