from selenium import webdriver
from selenium.webdriver.common.by import By
import time


def test_switching_to_the_constructor():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru")
    time.sleep(3)

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    time.sleep(3)

    driver.find_elements(By.NAME, 'name')[0].send_keys('testroman2000@mail.ru')
    driver.find_element(By.NAME, 'Пароль').send_keys('1234567')
    login_button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
    login_button.click()
    time.sleep(2)

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    time.sleep(3)
    
    driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
    time.sleep(2)
    driver.quit()


def test_switching_to_the_stellar_burgers_logo():
    driver = webdriver.Chrome()
    driver.get("https://stellarburgers.education-services.ru")
    time.sleep(3)

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    time.sleep(3)

    driver.find_elements(By.NAME, 'name')[0].send_keys('testroman2000@mail.ru')
    driver.find_element(By.NAME, 'Пароль').send_keys('1234567')
    login_button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
    login_button.click()
    time.sleep(2)

    driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
    time.sleep(3)

    driver.find_element(By.TAG_NAME, "svg").click()
    time.sleep(3)
    driver.quit()