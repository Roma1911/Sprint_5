import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from data import Logindata 

class TestNavigation:
    def test_switching_to_the_constructor(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.education-services.ru/")
        print("Шаг 1: Кликаем на «Личный кабинет»")
        personal_account_button = wait.until(EC.element_to_be_clickable(personal_account_button_main))
        personal_account_button.click()
        email_field = wait.until(EC.visibility_of_element_located(enter_reg_email))
        email_field.clear()
        email_field.send_keys(Logindata.email)  
        password_field = wait.until(EC.visibility_of_element_located(enter_reg_password))
        password_field.clear()
        password_field.send_keys(Logindata.password)
        login_button = wait.until(EC.element_to_be_clickable(enter_button_after_reg))
        login_button.click()
        constructor_btn = wait.until(EC.element_to_be_clickable(constructor_button))
        constructor_btn.click()
        constructor_title = wait.until(EC.visibility_of_element_located(constructor_button))
        assert constructor_title.is_displayed()

    def test_switching_to_the_stellar_burgers_logo(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.education-services.ru/")
        personal_account_button = wait.until(EC.element_to_be_clickable(personal_account_button_main))
        personal_account_button.click()
        email_field = wait.until(EC.visibility_of_element_located(enter_reg_email))
        email_field.clear()
        email_field.send_keys(Logindata.email)
        password_field = wait.until(EC.visibility_of_element_located(enter_reg_password))
        password_field.clear()
        password_field.send_keys(Logindata.password)
        login_button = wait.until(EC.element_to_be_clickable(enter_button_after_reg))
        login_button.click()
        logo_element = wait.until(EC.element_to_be_clickable(logo))
        logo_element.click()
        main_page_title = wait.until(EC.visibility_of_element_located(logo))
        assert main_page_title.is_displayed()