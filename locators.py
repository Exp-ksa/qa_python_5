from selenium.webdriver.common.by import By

class Registration_Locators:
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[@type='text']")
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    LINK_LOGIN = (By.CSS_SELECTOR, "a.Auth_link__1fOlj")
    
class Login_Locators:
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_medium__3zxIa")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LINK_REGISTRATION = (By.XPATH, ".//a[@href='/register']")
    LINK_FOGOT_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")

class Fogot_Locators:
    LINK_FOGOT_PASSWORD = (By.CSS_SELECTOR, "a.Auth_link__1fOlj")

class Profile_Locators:
    EXIT_BUTTON = (By.CSS_SELECTOR, "Account_button__14Yp3.text.text_type_main-medium.text_color_inactive")

class Main_Locators:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "button.header__logout")
    SUCCESSFUL_REGISTER_POPUP = (By.CSS_SELECTOR, "p.popup__status-message")