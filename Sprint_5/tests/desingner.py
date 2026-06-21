import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from locators import *

class TestTabs:
    
    def test_sauces_tab(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.education-services.ru")
        wait.until(EC.element_to_be_clickable(sauces_button)).click()
        wait.until(EC.element_to_be_clickable(sauce_spicy_x_image)).click()
        sauces_element = wait.until(EC.visibility_of_element_located(sauces_text))
        assert sauces_element.is_enabled()

    def test_fillings_tab(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.education-services.ru")
        wait.until(EC.element_to_be_clickable(filling_button)).click()
        wait.until(EC.element_to_be_clickable(meat_immortal_mollusks_image)).click()
        fillings_element = wait.until(EC.visibility_of_element_located(fillings_text))
        assert fillings_element.is_enabled()
    
    def test_buns_tab(self, driver):
        wait = WebDriverWait(driver, 10)
        driver.get("https://stellarburgers.education-services.ru")
        wait.until(EC.element_to_be_clickable(sauces_button)).click()
        wait.until(EC.element_to_be_clickable(buns_button)).click()
        wait.until(EC.element_to_be_clickable(fluorescent_bun_r2_d3_image)).click()
        buns_element = wait.until(EC.visibility_of_element_located(buns_text))
        assert buns_element.is_enabled()