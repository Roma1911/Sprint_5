
import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from data import Logindata

class TestLogoutOfAccount:
    def test_exit_via_logout_button(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.education-services.ru/")
        personal_account_btn = wait.until(EC.element_to_be_clickable(personal_account_button_main))
        personal_account_btn.click()
        email_field = wait.until(EC.visibility_of_element_located(enter_reg_email))
        email_field.send_keys(Logindata.email)
        password_field = wait.until(EC.visibility_of_element_located(login_password_field))
        password_field.send_keys(Logindata.password) 
        login_btn = wait.until(EC.element_to_be_clickable(click_login_button))
        login_btn.click()
        wait.until(EC.visibility_of_element_located(personal_account_button_main))
        personal_account_after_login = wait.until(EC.element_to_be_clickable(personal_account_button_main))
        personal_account_after_login.click()
        login_btn_after_logout = wait.until(EC.visibility_of_element_located(logout_button))
        login_btn_after_logout.click()
        assert login_btn_after_logout.is_displayed()