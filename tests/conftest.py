import pytest
from selenium import webdriver
from data.urls import BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()