from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Login_Locators, Main_Locators

class TestRedirects:

    def test_personal_account_button_redirects_to_login(self, main_page):

        driver = main_page
        driver.find_element(*Main_Locators.PERSONAL_ACCOUNT_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Login_Locators.LOGIN_BUTTON))

        assert "login" in driver.current_url 
    
    def test_constructor_button_from_profile_redirects_to_main(self, login_page):
        
        driver = login_page
        driver.find_element(*Login_Locators.CONSTRUCTOR_BUTTON).click()
        
        buns_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.BUNS_BUTTON))

        assert buns_button.text == 'Булки'

    def test_logo_from_profile_redirects_to_main(self, login_page):

        driver = login_page
        driver.find_element(*Login_Locators.STELLAR_BURGER_LOGO).click()
        
        buns_button = WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.BUNS_BUTTON))

        assert buns_button.text == 'Булки'