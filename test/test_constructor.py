import pytest

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from locators import Main_Locators

class TestConstuctor:

    @pytest.mark.parametrize('button, find, ingredients', 
                             [
                                 [Main_Locators.SAUCES_BUTTON,Main_Locators.SAUCES_TEXT,'Соусы'], 
                                 [Main_Locators.FILLINGS_BUTTON, Main_Locators.FILLINGS_TEXT,'Начинки'],
                                 [Main_Locators.BUNS_BUTTON, Main_Locators.BUNS_TEXT, 'Булки']
                             ])
    def test_ingredients_section_click_opens_ingredients(self, main_page, button, find, ingredients):
        
        driver = main_page
        if button == Main_Locators.BUNS_BUTTON:
            driver.find_element(*Main_Locators.FILLINGS_TEXT).click()
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.FILLINGS_TEXT))
            
        driver.find_element(*button).click()
        
        element = driver.find_element(*find)
        driver.execute_script("arguments[0].scrollIntoView();", element) 
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(find))

        assert element.text == ingredients