from selenium.webdriver.common.by import By

# Локаторы для авторизации и входа
login_email_field = (By.XPATH, "//input[@type='email']")
login_password_field = (By.XPATH, "//input[@type='password' and contains(@name, 'Пароль')]")
click_login_button = (By.XPATH, "//button[contains(text(), 'Войти')]")
personal_account_button_main = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
enter_to_account_main = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт') and contains(@class, 'button_button')]")

# Локаторы для регистрации
enter_reg_name = (By.XPATH, "//label[contains(text(), 'Имя')]//following-sibling::input[@type='text']")
enter_reg_email = (By.XPATH, "//label[contains(text(), 'Email')]//following-sibling::input[@type='text']")
enter_reg_password = (By.XPATH, "//input[contains(@name, 'Пароль') and @type='password']")
click_reg_button = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться') and contains(@class, 'button_button')]")
enter_button_after_reg = (By.XPATH, "//button[contains(text(), 'Войти') and contains(@class, 'button_button')]")
not_correct_password = (By.XPATH, "//p[contains(@class, 'input__error')]")

# Локаторы для личного кабинета и выхода
logout_button = (By.XPATH, "//button[contains(text(), 'Выход')]")
order_history = (By.XPATH, "//a[contains(@class, 'Account_link') and contains(text(), 'История заказов')]")

# Локаторы для навигации
constructor_button = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
logo = (By.TAG_NAME, "svg")
main_title_of_constructor = (By.XPATH, "//h1[contains(text(), 'Конструктор')]")

# Локаторы для вкладок конструктора
buns_button = (By.XPATH, "//span[contains(text(), 'Булки')]/parent::*")
sauces_button = (By.XPATH, "//span[contains(text(), 'Соусы')]/parent::*")
filling_button = (By.XPATH, "//span[contains(text(), 'Начинки')]/parent::*")
buns_text = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and contains(text(), 'Булки')]")
fillings_text = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and contains(text(), 'Начинки')]")
sauces_text = (By.XPATH, "//h2[contains(@class, 'text_type_main-medium') and contains(text(), 'Соусы')]")
main_title_of_constructor = (By.XPATH, "//h1[contains(@class, 'text_type_main-large') and contains(text(), 'Конструктор')]")
logo_by_class = (By.XPATH, "//svg[contains(@class, 'logo')]")  

# Ссылки для восстановления пароля и регистрации
register_link = (By.XPATH, "//a[contains(text(), 'Зарегистрироваться')]")
forgot_password_link = (By.XPATH, "//a[contains(text(), 'Восстановить пароль')]")
enter_button_from_forgot_password_page = (By.XPATH, "//a[contains(text(), 'Войти')]")

sauce_spicy_x_image = (By.XPATH,"//img[@alt='Соус Spicy-X' and contains(@class, 'BurgerIngredient_ingredient__image')]")
meat_immortal_mollusks_image = (By.XPATH,"//img[@alt='Мясо бессмертных моллюсков Protostomia' and contains(@class, 'BurgerIngredient_ingredient__image')]")
fluorescent_bun_r2_d3_image = (By.XPATH,"//img[@alt='Флюоресцентная булка R2-D3' and contains(@class, 'BurgerIngredient_ingredient__image')]")
