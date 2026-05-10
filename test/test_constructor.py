from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..locators import Main_Locators

class TestConstuctor:
    def test_sauces_section_click_opens_sauces(self, main_page):
        
        driver = main_page
        driver.find_element(*Main_Locators.SAUCES_BUTTON).click()

        sauces = driver.find_element(*Main_Locators.SAUCES_TEXT)
        driver.execute_script("arguments[0].scrollIntoView();", sauces) 
        
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.SAUCES_TEXT))

        assert sauces.text == 'Соусы'

    def test_fillings_section_click_opens_fillings(self, main_page):
        
        driver = main_page
        driver.find_element(*Main_Locators.FILLINGS_BUTTON).click()

        fillings = driver.find_element(*Main_Locators.FILLINGS_TEXT)
        driver.execute_script("arguments[0].scrollIntoView();", fillings)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.FILLINGS_TEXT))

        assert fillings.text == 'Начинки'

    def test_buns_section_click_opens_buns(self, main_page):
        
        driver = main_page
        driver.find_element(*Main_Locators.FILLINGS_BUTTON).click()
        
        fillings = driver.find_element(*Main_Locators.FILLINGS_TEXT)
        driver.execute_script("arguments[0].scrollIntoView();", fillings)

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.FILLINGS_TEXT))

        driver.find_element(*Main_Locators.BUNS_BUTTON).click()
        buns = driver.find_element(*Main_Locators.BUNS_TEXT)
        driver.execute_script("arguments[0].scrollIntoView();", buns)
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(Main_Locators.BUNS_TEXT))

        assert buns.text == 'Булки'