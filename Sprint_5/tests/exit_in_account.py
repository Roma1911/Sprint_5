
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from data import Logindata

class TestLogoutOfAccount:
    def test_exit_via_logout_button(self, driver):
        wait = WebDriverWait(driver, 15)
        driver.get("https://stellarburgers.education-services.ru/")
        personal_account_btn = wait.until(
            EC.element_to_be_clickable(personal_account_button_main)
        )
        personal_account_btn.click()
        email_field = wait.until(
            EC.visibility_of_element_located(login_email_field)
        )
        email_field.clear()
        email_field.send_keys(Logindata.email)
        password_field = driver.find_element(*login_password_field)
        password_field.clear()
        password_field.send_keys(Logindata.password)
        login_btn = wait.until(
            EC.element_to_be_clickable(click_login_button)
        )
        login_btn.click()
        wait.until(EC.visibility_of_element_located(personal_area_text))
        personal_account_btn_header = wait.until(
            EC.element_to_be_clickable(personal_account_button_main)
        )
        personal_account_btn_header.click()
        logout_btn = wait.until(
            EC.element_to_be_clickable(logout_button)
        )
        logout_btn.click()
        login_button = wait.until(
            EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Войти')]"))
        )
        assert login_button.is_displayed()