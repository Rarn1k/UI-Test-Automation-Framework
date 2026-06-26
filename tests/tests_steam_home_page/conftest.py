import pytest
from selenium import webdriver

from page_objects.home_page import HomePage


@pytest.fixture
def home_page(driver: webdriver) -> HomePage:
    return HomePage(driver)
