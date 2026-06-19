import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import RegistrationData


class TestSimpleRegistration:

    def test_complete_registration(self, driver):
        wait = WebDriverWait(driver, 15)
        unique_name = RegistrationData.generate_unique_name()
        unique_email = RegistrationData.generate_unique_email()
        valid_password  = RegistrationData.generate_strong_password()
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.presence_of_element_located(enter_reg_name))
        name_field = driver.find_element(*enter_reg_name)
        name_field.clear()
        name_field.send_keys(unique_name)
        wait.until(EC.presence_of_element_located(enter_reg_email))
        email_field = driver.find_element(*enter_reg_email)
        email_field.clear()
        email_field.send_keys(unique_email)
        wait.until(EC.presence_of_element_located(enter_reg_password))
        password_field = driver.find_element(*enter_reg_password)
        password_field.clear()
        password_field.send_keys(valid_password)
        wait.until(EC.element_to_be_clickable(click_reg_button))
        reg_button = driver.find_element(*click_reg_button)
        reg_button.click()
        wait.until(EC.element_to_be_clickable(enter_button_after_reg))
        login_button = driver.find_element(*enter_button_after_reg)
        assert login_button.is_displayed()
        print(f"Регистрация успешна! Пользователь: {unique_name}, Email: {unique_email}")

    def test_invalid_password_validation(self, driver):
        wait = WebDriverWait(driver, 15)
        unique_email = RegistrationData.generate_unique_email()
        unique_name = RegistrationData.generate_unique_name()
        invalid_password = "123"
        driver.get("https://stellarburgers.education-services.ru/register")
        wait.until(EC.presence_of_element_located(enter_reg_name))
        name_field = driver.find_element(*enter_reg_name)
        name_field.clear()
        name_field.send_keys(unique_name)
        wait.until(EC.presence_of_element_located(enter_reg_email))
        email_field = driver.find_element(*enter_reg_email)
        email_field.clear()
        email_field.send_keys(unique_email)
        wait.until(EC.presence_of_element_located(enter_reg_password))
        password_field = driver.find_element(*enter_reg_password)
        password_field.clear()
        password_field.send_keys(invalid_password)
        wait.until(EC.element_to_be_clickable(click_reg_button))
        reg_button = driver.find_element(*click_reg_button)
        reg_button.click()
        wait.until(EC.visibility_of_element_located(not_correct_password))
        error_element = driver.find_element(*not_correct_password)
        assert error_element.is_displayed()