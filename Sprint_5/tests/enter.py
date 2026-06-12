from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_button_log_in_to_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru")
    time.sleep(3)

    driver.find_element(By.XPATH,"//button[contains(text(), 'Войти в аккаунт')]").click()

    email_element = driver.find_elements(By.NAME, 'name')[0]
    email_element.send_keys('testroman2000@mail.ru')

    password_element = driver.find_element(By.NAME, 'Пароль')
    password_element.send_keys('1234567')

    login_button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
    login_button.click()

    time.sleep(3)
    driver.quit()


def test_button_personal_account():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru")
    time.sleep(3)

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    time.sleep(5)

    email_element = driver.find_elements(By.NAME, 'name')[0]
    email_element.send_keys('testroman2000@mail.ru')

    password_element = driver.find_element(By.NAME, 'Пароль')
    password_element.send_keys('1234567')
     
    login_button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
    login_button.click()

    time.sleep(3)
    driver.quit()


def test_button_form_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru")
    time.sleep(3)
       
    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, ".//a[text()='Зарегистрироваться']").click()
    time.sleep(2)

    login_button = driver.find_element(By.XPATH, ".//a[text()='Войти']")
    login_button.click()
    time.sleep(2)

    driver.find_elements(By.NAME, 'name')[0].send_keys('testroman2000@mail.ru')
    driver.find_element(By.NAME, 'Пароль').send_keys('1234567')
    login_button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
    login_button.click()

    time.sleep(3)
    driver.quit()


def test_button_in_the_password_recovery_form():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru")
    time.sleep(3)

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    time.sleep(2)

    driver.find_element(By.XPATH, ".//a[text()='Восстановить пароль']").click()
    time.sleep(2)
    
    driver.find_element(By.XPATH, ".//a[text()='Войти']").click()
    time.sleep(2)

    driver.find_elements(By.NAME, 'name')[0].send_keys('testroman2000@mail.ru')
    driver.find_element(By.NAME, 'Пароль').send_keys('1234567')
    login_button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
    login_button.click()

    time.sleep(3)
    driver.quit()
