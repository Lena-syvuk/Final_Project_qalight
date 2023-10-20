import pytest
from selenium import webdriver

@pytest.fixture()

def chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(60)
    yield driver
    driver.quit()