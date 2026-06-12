from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_successful_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")
    time.sleep(3)

    driver.find_element(By.NAME, 'name').send_keys('Roman')

    driver.find_elements(By.NAME, 'name')[1].send_keys('testroman2000@mail.ru')

    driver.find_element(By.NAME, 'Пароль').send_keys('123456')

    driver.find_element(By.XPATH,"//button[contains(text(), 'Зарегистрироваться')]").click()

    time.sleep(3)
    driver.quit()


def test_not_correct_password_error_for_registration():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru/register")
    time.sleep(3)

    driver.find_element(By.NAME, 'name').send_keys('Roman')

    driver.find_elements(By.NAME, 'name')[1].send_keys('testroman2000@mail.ru')

    driver.find_element(By.NAME, 'Пароль').send_keys('123')

    driver.find_element(By.XPATH,"//button[contains(text(), 'Зарегистрироваться')]").click()

    time.sleep(3)
    driver.quit()
