import os
import sys
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from locators.base_page_locators import BASE_URL


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))


@pytest.fixture
def driver():
    options = Options()
    driver = webdriver.Firefox(options=options)
    driver.get(BASE_URL)
    driver.maximize_window()
    yield driver
    driver.quit()