
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *

class TestPersonalAccount:

    def test_click_on_personal_account(self, driver):
        wait = WebDriverWait(driver, 10)  
        personal_account_button = wait.until(EC.element_to_be_clickable(personal_account_button_main))
        personal_account_button.click()
        email_field = wait.until(EC.visibility_of_element_located(enter_reg_email))
        email_field.send_keys("testroman2000@mail.ru")
        password_field = wait.until(EC.visibility_of_element_located(login_password_field))
        password_field.send_keys("1234567")
        login_button = wait.until(EC.element_to_be_clickable(enter_button_after_reg))
        login_button.click()
        personal_area_element = wait.until(EC.visibility_of_element_located(personal_account_button_main))
        assert personal_area_element.is_displayed()
        