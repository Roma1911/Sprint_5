from selenium import webdriver
from selenium.webdriver.common.by import By
from locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Testclickconstructorandstellarburgerslogo:

    def test_switching_to_the_constructor(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        driver.find_elements(By.NAME, 'name')[0].send_keys('testroman2000@mail.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('1234567')
        login_button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
        login_button.click()
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        driver.find_element(By.XPATH, ".//p[text()='Конструктор']").click()
        wait = WebDriverWait(driver, 10)
        constructor_title = wait.until(
            EC.visibility_of_element_located((By.XPATH, ".//p[text()='Конструктор']"))
        )
        assert constructor_title.is_displayed()
        driver.quit()

    def test_switching_to_the_stellar_burgers_logo(self):
        driver = webdriver.Chrome()
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        driver.find_elements(By.NAME, 'name')[0].send_keys('testroman2000@mail.ru')
        driver.find_element(By.NAME, 'Пароль').send_keys('1234567')
        login_button = driver.find_element(By.CLASS_NAME, 'button_button__33qZ0')
        login_button.click()
        driver.find_element(By.XPATH, ".//p[text()='Личный Кабинет']").click()
        driver.find_element(By.TAG_NAME, "svg").click()
        wait = WebDriverWait(driver, 10)
        main_page_element = wait.until(
            EC.visibility_of_element_located((By.XPATH, ".//p[text()='Конструктор']"))
        )
        assert main_page_element.is_displayed()