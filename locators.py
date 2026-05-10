from selenium.webdriver.common.by import By

class Registration_Locators: #Страница "Регистации"
    #Поле имя
    NAME_FIELD = (By.XPATH, ".//label[text()='Имя']/following-sibling::input[@type='text']")
    #Поле Email
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    #Поле пароль
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")
    #Кнопка "Зарегистрироваться"
    REGISTER_BUTTON = (By.XPATH, ".//button[text() ='Зарегистрироваться']")
    #Ссылка на страницу логин
    LINK_LOGIN = (By.CSS_SELECTOR, "a.Auth_link__1fOlj")
    #Сообщение "Некорректный пароль"
    INCORRECT_PASSWORD = (By.CSS_SELECTOR, 'p.input__error.text_type_main-default')
    
class Login_Locators: #Страница "Личный кабинет"
    #Поле Email
    EMAIL_FIELD = (By.XPATH, ".//label[text()='Email']/following-sibling::input[@type='text']")
    #Поле пароль
    PASSWORD_FIELD = (By.XPATH, ".//input[@type='password']")
    #Кнопка "Войти"
    LOGIN_BUTTON = (By.XPATH, ".//button[text() ='Войти']")
    #Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    #Логотип "Stellar Burgers"
    STELLAR_BURGER_LOGO = (By.CSS_SELECTOR, "div.AppHeader_header__logo__2D0X2")
    #Ссылка на страницу "Регистрации" 
    LINK_REGISTRATION = (By.XPATH, ".//a[@href='/register']")
    #Ссылка на страницу "Восстановления пароля"
    LINK_FOGOT_PASSWORD = (By.XPATH, ".//a[@href='/forgot-password']")
    
class Forgot_Locators: #Страница "Восстановление пароля"
    #Ссылка в "Личный кабинет"
    LINK_LOGIN = (By.CSS_SELECTOR, "a.Auth_link__1fOlj")

class Profile_Locators: #Страница "Личного Кабинета"
    #Кнопка "Выход"
    EXIT_BUTTON = (By.XPATH, ".//button[@type = 'button' and text()='Выход']")

class Main_Locators: #Гланое страница конструктор
    #Кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href='/account']")
    #Кнопка "Войти в аккаунт"
    LOGIN_ACCAUNT_BUTTON = (By.CSS_SELECTOR, 'button.button_button__33qZ0.button_button_type_primary__1O7Bx.button_button_size_large__G21Vg')
    #Кнопка "Булки"
    BUNS_BUTTON = (By.XPATH, ".//span[text()='Булки']")
    #Наименование "Булки" в списке булок
    BUNS_TEXT = (By.XPATH, ".//h2[text()= 'Булки']")
    #Кнопка "Соусы"
    SAUCES_BUTTON = (By.XPATH, ".//span[text()='Соусы']")
    #Наименование "Соусы" в списке булок
    SAUCES_TEXT = (By.XPATH, ".//h2[text()= 'Соусы']")
    #Кнопка "Начинки"
    FILLINGS_BUTTON = (By.XPATH, ".//span[text()='Начинки']")
    #Наименование "Начинки" в списке булок
    FILLINGS_TEXT = (By.XPATH, ".//h2[text()= 'Начинки']")
    #Кнопка "Оформить заказ"
    ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    