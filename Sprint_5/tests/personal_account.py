import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *

class TestPersonalAccount:

    def test_click_on_personal_account(self, driver):
        driver.get("https://stellarburgers.education-services.ru")
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable(personal_account_button_main)).click()
        wait.until(EC.visibility_of_element_located(login_email_field)).send_keys("testuser123rom@mail.ru")
        driver.find_element(*login_password_field).send_keys("12345672578")
        wait.until(EC.element_to_be_clickable(click_login_button)).click()
        assert wait.until(EC.visibility_of_element_located(personal_area_text))