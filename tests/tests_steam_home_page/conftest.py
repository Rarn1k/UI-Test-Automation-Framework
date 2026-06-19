import pytest

from page_objects.home_page import HomePage
from web_driver.chrome_driver import ChromeDriver


@pytest.fixture
def home_page(driver):
    return HomePage(driver).get()
