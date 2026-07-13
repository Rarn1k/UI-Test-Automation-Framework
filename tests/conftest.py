from typing import Any, Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from web_driver.driver import Driver



@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, Any, None]:
    driver_wrapper = Driver()
    driver_wrapper.get_driver().maximize_window()
    yield driver_wrapper.get_driver()
    driver_wrapper.quit()
