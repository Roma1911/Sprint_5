import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import *


class TestTabs:
    
    def test_sauces_tab(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.education-services.ru/")
        wait.until(EC.element_to_be_clickable(sauces_button)).click()
        sauces_element = wait.until(EC.visibility_of_element_located(sauces_text))
        assert sauces_element.is_displayed()

    def test_fillings_tab(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.education-services.ru/")
        wait.until(EC.element_to_be_clickable(filling_button)).click()
        fillings_element = wait.until(EC.visibility_of_element_located(fillings_text))
        assert fillings_element.is_displayed()
    
    def test_buns_tab(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.education-services.ru/")
        buns_button_element = wait.until(EC.element_to_be_clickable(buns_button))
        driver.execute_script("arguments[0].scrollIntoView(true);", buns_button_element)
        driver.execute_script("arguments[0].click();", buns_button_element)
        buns_element = wait.until(EC.visibility_of_element_located(buns_text))
        assert buns_element.is_displayed()