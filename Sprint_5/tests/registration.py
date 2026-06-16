import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *
from data import RegistrationData  
from time import sleep

class TestRegistration:

    def test_user_registration(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        wait = WebDriverWait(driver, 10)
        driver.find_element(*enter_reg_name).send_keys(RegistrationData.valid_name)
        driver.find_element(*enter_reg_email).send_keys(RegistrationData.valid_email)
        driver.find_element(*enter_reg_password).send_keys(RegistrationData.valid_password)
        driver.find_element(*click_reg_button).click()
        wait.until(EC.element_to_be_clickable(enter_button_after_reg))
        login_button = driver.find_element(*enter_button_after_reg)
        assert login_button.is_displayed()

    def test_password_error(self, driver):
        driver.get("https://stellarburgers.education-services.ru/register")
        wait = WebDriverWait(driver, 10)
        driver.find_element(*enter_reg_name).send_keys(RegistrationData.valid_name)
        driver.find_element(*enter_reg_email).send_keys(RegistrationData.invalid_email)
        driver.find_element(*enter_reg_password).send_keys(RegistrationData.invalid_password)
        driver.find_element(*click_reg_button).click()
        wait.until(EC.visibility_of_element_located(not_correct_password))
        error_element = driver.find_element(*not_correct_password)
        sleep(2)
        assert error_element.is_displayed()