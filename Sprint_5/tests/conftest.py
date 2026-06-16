import pytest
from selenium import webdriver

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    try:
        yield driver
    finally:
        driver.quit()

