import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestLoginScenarios:
    def setup_method(self):
        self.email = "testuser123rm@mail.ru"
        self.password = "12345672578"

    def test_login_via_main_button(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable(enter_to_account_main)).click()
        email_field = wait.until(EC.visibility_of_element_located(login_email_field))
        email_field.clear()
        email_field.send_keys(self.email)
        password_field = wait.until(EC.visibility_of_element_located(login_password_field))
        password_field.clear()
        password_field.send_keys(self.password)
        login_btn = wait.until(EC.element_to_be_clickable(click_login_button))
        login_btn.click()
        assert wait.until(EC.visibility_of_element_located(personal_area_text)).is_displayed()
    def test_login_via_personal_account(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable(personal_account_button_main)).click()
        email_field = wait.until(EC.visibility_of_element_located(login_email_field))
        email_field.clear()
        email_field.send_keys(self.email)
        password_field = wait.until(EC.visibility_of_element_located(login_password_field))
        password_field.clear()
        password_field.send_keys(self.password)
        login_btn = wait.until(EC.element_to_be_clickable(click_login_button))
        login_btn.click()
        assert wait.until(EC.visibility_of_element_located(personal_area_text)).is_displayed()

    def test_login_via_registration_form(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable(personal_account_button_main)).click()
        wait.until(EC.element_to_be_clickable(register_link)).click()
        wait.until(EC.element_to_be_clickable(enter_button_from_forgot_password_page)).click()
        email_field = wait.until(EC.visibility_of_element_located(login_email_field))
        email_field.clear()
        email_field.send_keys(self.email)
        password_field = wait.until(EC.visibility_of_element_located(login_password_field))
        password_field.clear()
        password_field.send_keys(self.password)
        login_btn = wait.until(EC.element_to_be_clickable(click_login_button))
        login_btn.click()
        assert wait.until(EC.visibility_of_element_located(personal_area_text)).is_displayed()


    def test_login_via_forgot_password(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable(personal_account_button_main)).click()
        wait.until(EC.element_to_be_clickable(forgot_password_link)).click()
        wait.until(EC.element_to_be_clickable(enter_button_from_forgot_password_page)).click()
        email_field = wait.until(EC.visibility_of_element_located(login_email_field))
        email_field.clear()
        email_field.send_keys(self.email)
        password_field = wait.until(EC.visibility_of_element_located(login_password_field))
        password_field.clear()
        password_field.send_keys(self.password)
        login_btn = wait.until(EC.element_to_be_clickable(click_login_button))
        login_btn.click()
        assert wait.until(EC.visibility_of_element_located(personal_area_text)).is_displayed()