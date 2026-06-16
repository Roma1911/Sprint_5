
from selenium.webdriver.common.by import By

# # Локаторы для авторизации и входа
login_email_field = (By.XPATH, "//input[@type='email']")
login_email_field = (By.XPATH, "//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
login_password_field = (By.XPATH, "//input[@type='password' and @name='Пароль']")
click_login_button = (By.XPATH, "//button[text()='Войти']")
personal_account_button_main = (By.XPATH, "//p[text()='Личный Кабинет']")
enter_to_account_main = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт') and contains(@class, 'button_button__33qZ0')]")

# # Локаторы для регистрации
enter_reg_name = (By.XPATH, "//label[text()='Имя']//parent::*/input[@type='text' and @name='name']")
enter_reg_email = (By.XPATH, "//label[text()='Email']//parent::*/input[@type='text' and @name='name']")
enter_reg_password = (By.XPATH, "//input[@name='Пароль' and @type='password' and @class='text input__textfield text_type_main-default']")
click_reg_button = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Зарегистрироваться']")
enter_button_after_reg = (By.XPATH, "//button[@class='button_button__33qZ0 button_button_type_primary__1O7Bx button_button_size_medium__3zxIa' and text()='Войти']")
not_correct_password = (By.XPATH, "//p[contains(@class, 'input__error')]")
personal_account_button_main = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")

# #   Локаторы для личного кабинета и выхода
personal_area_text = (By.XPATH, "//p[text()='Личный Кабинет']")
logout_button = (By.XPATH, "//button[text()='Выход']")
order_history = (By.XPATH, "//li[@class='Account_listItem__35dAP']/a[@class='Account_link__2ETsJ text text_type_main-medium text_color_inactive']")

# #  Локаторы для навигации
constructor_button = (By.XPATH, "//p[text()='Конструктор']")
logo = (By.TAG_NAME, "svg")
main_title_of_constructor = (By.XPATH, "//h1[contains(text(), 'Конструктор')]")

# #  Локаторы для вкладок конструктора
buns_button = (By.XPATH, "//span[text()='Булки']/parent::*")
sauces_button = (By.XPATH, "//span[text()='Соусы']/parent::*")
filling_button = (By.XPATH, "//span[text()='Начинки']/parent::*")
buns_text = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Булки']")
fillings_text = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Начинки']")
sauces_text = (By.XPATH, "//h2[@class='text text_type_main-medium mb-6 mt-10' and text()='Соусы']")
main_title_of_constructor = (By.XPATH, "//h1[@class='text text_type_main-large mt-10 mb-6' and text()='Конструктор']")
logo = (By.XPATH, "//svg[@width='290' and @height='50']")

# #  Ссылки для восстановления пароля и регистрации
register_link = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
forgot_password_link = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
enter_button_from_forgot_password_page = (By.XPATH, ".//a[text()='Войти']")

constructor_buttonz = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
constructor_buttons = (By.XPATH, "//p[@class='AppHeader_header__linkText__3q_va ml-2' and contains(text(), 'Конструктор')]")
constructor_buttont = (By.XPATH, "//p[contains(@class, 'AppHeader_header__linkText') and contains(text(), 'Конструктор')]")

logos = (By.XPATH, "//svg[@width='290' and @height='50']") 
logoz = (By.XPATH, "//svg[@xmlns='http://www.w3.org/2000/svg']") 
logot = (By.XPATH, "//svg[@width='290' and @height='50' and contains(@class, 'AppHeader')]") 
logor = (By.CSS_SELECTOR, "svg.AppHeader_header__logo__22rsg")