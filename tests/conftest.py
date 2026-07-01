from typing import Any, Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from web_driver.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, Any, None]:
    yield DriverFactory().create_driver().get_driver()
    DriverFactory().create_driver().get_driver().quit()
