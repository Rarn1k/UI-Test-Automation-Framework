from typing import Any, Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from utils.config.config_manager import ConfigManager
from web_driver.driver import Driver
from web_driver.driver_factory import DriverFactory


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, Any, None]:
    yield Driver().get_driver()
    Driver().quit()
