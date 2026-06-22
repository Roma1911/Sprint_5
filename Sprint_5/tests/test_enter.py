import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *
from data import TestLoginScenarios

class TestLoginProcess:

    def test_login_via_main_button(self, driver):
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable(enter_to_account_main)).click()
        email_field = wait.until(EC.visibility_of_element_located(enter_reg_email))
        email_field.send_keys(TestLoginScenarios.email)
        password_field = wait.until(EC.visibility_of_element_located(login_password_field))
        password_field.send_keys(TestLoginScenarios.password)
        login_btn = wait.until(EC.element_to_be_clickable(click_login_button))
        login_btn.click()
        personal_account_element = wait.until(EC.visibility_of_element_located(personal_account_button_main))
        assert personal_account_element.is_displayed()

    def test_login_via_personal_account(self, driver):
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable(personal_account_button_main)).click()
        email_field = wait.until(EC.visibility_of_element_located(enter_reg_email))
        email_field.send_keys(TestLoginScenarios.email)
        password_field = wait.until(EC.visibility_of_element_located(login_password_field))
        password_field.send_keys(TestLoginScenarios.password)
        login_btn = wait.until(EC.element_to_be_clickable(click_login_button))
        login_btn.click()
        personal_account_element = wait.until(EC.visibility_of_element_located(personal_account_button_main))
        assert personal_account_element.is_displayed()

    def test_login_via_registration_form(self, driver):
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable(personal_account_button_main)).click()
        wait.until(EC.element_to_be_clickable(register_link)).click()
        wait.until(EC.element_to_be_clickable(enter_button_from_forgot_password_page)).click()
        email_filed = wait.until(EC.visibility_of_element_located(enter_reg_email))
        email_filed.send_keys(TestLoginScenarios.email)
        password_filed = wait.until(EC.visibility_of_element_located(login_password_field))
        password_filed.send_keys(TestLoginScenarios.password)
        login_btn = wait.until(EC.element_to_be_clickable(click_login_button))
        login_btn.click()
        personal_account_element = wait.until(EC.visibility_of_element_located(personal_account_button_main))
        assert personal_account_element.is_displayed()

    def test_login_via_forgot_password(self, driver):
        wait = WebDriverWait(driver, 15)
        wait.until(EC.element_to_be_clickable(personal_account_button_main)).click()
        wait.until(EC.element_to_be_clickable(forgot_password_link)).click()
        wait.until(EC.element_to_be_clickable(enter_button_from_forgot_password_page)).click()
        email_field = wait.until(EC.visibility_of_element_located(enter_reg_email))
        email_field.send_keys(TestLoginScenarios.email)
        password_field = wait.until(EC.visibility_of_element_located(login_password_field))
        password_field.send_keys(TestLoginScenarios.password)
        login_btn = wait.until(EC.element_to_be_clickable(click_login_button))
        login_btn.click()
        personal_account_element = wait.until(EC.visibility_of_element_located(personal_account_button_main))
        assert personal_account_element.is_displayed()