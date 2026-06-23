import pytest

from page_objects.home_page import HomePage


@pytest.fixture
def home_page(driver):
    return HomePage(driver)
