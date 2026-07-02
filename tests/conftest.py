from typing import Any, Generator

import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from utils.get_marker_path import GetMarkerPath
from web_driver.driver import Driver

import logging

root = GetMarkerPath.get_marker_path()
log_path = root / "logs/test.log"
log_path.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    filename="logs/test.log",
    filemode="w",
    encoding="utf-8"
)


@pytest.fixture(scope="function")
def driver() -> Generator[WebDriver, Any, None]:
    driver_wrapper = Driver()
    driver_wrapper.get_driver().maximize_window()
    yield driver_wrapper.get_driver()
    driver_wrapper.quit()
