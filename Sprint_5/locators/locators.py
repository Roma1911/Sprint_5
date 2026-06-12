# Заголовок...https://stellarburgers.education-services.ru/registar

Имя = driver.find_element(By.NAME, 'name').send_keys('Roman')

Email = driver.find_elements(By.NAME, 'name').send_keys('testroman2000@mail.ru')

Пароль = driver.find_element(By.NAME, 'Пароль').send_keys('1234567')

Кнопка зарегестрироваться = driver.find_element(By.XPATH,"//button[contains(text(), 'Зарегистрироваться')]")

# Заголовок = https://stellarburgers.education-services.ru/personal_account

Кнопка Личный Кабинет = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']")

Кнопка Войти = login_button=driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')

# Заголовок...https://stellarburgers.education-services.ru/exit_in_account

Кнопка Личный Кабинет = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']")

Кнопка Войти = login_button=driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')

Кнопка Выход = login_button=driver.find_element(By.CLASS_NAME, 'Account_button__14Yp3')

# Заголовок...https://stellarburgers.education-services.ru/enter

test_button_log_in_to_account
Кнопка Войти в аккаунт = driver.find_element(By.XPATH,"//button[contains(text(), 'Войти в аккаунт')]")
Кнопка Войти = login_button=driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')

test_button_personal_account
нопка Личный Кабинет = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']")
Кнопка Войти = login_button=driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
test_button_form_registration
Кнопка Личный Кабинет = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']")
Кнопка Зарегестрироваться = driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']")
Кнопка Войти...login_button=driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')

test_button_in_the_password_recovery_form
Кнопка Личный Кабинет = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']")
Кнопка Восстановить Пароль = driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']")
Кнопка Войти = driver.find_element(By.XPATH, ".//a[text()='Войти']")

# Заголовок...https://stellarburgers.education-services.ru/desingner

Кнопка Личный Кабинет = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']")

Раздел Конструктор = driver.find_element(By.XPATH, ".//p[text()='Конструктор']")

Раздел Соусы = driver.find_element(By.XPATH, ".//span[text()='Соусы']")

Раздел Начинки = driver.find_element(By.XPATH, ".//span[text()='Начинки']")

Раздел Булки = driver.find_element(By.XPATH, ".//span[text()='Булки']")

# Заголовок...https://stellarburgers.education-services.ru/designer_and_stellar_burgers

test_switching_to_the_constructor
Кнопка Личный Кабинет = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']")
Кнопка Войти = login_button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
Раздел Конструктор = driver.find_element(By.XPATH, ".//p[text()='Конструктор']")
test_switching_to_the_stellar_burgers_logo
Кнопка Личный Кабинет = driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']")
Кнопка Войти = login_button=driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
Логотип Stellar Burgers = driver.find_element(By.TAG_NAME, "svg")
