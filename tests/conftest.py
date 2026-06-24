import pytest

from utils.config.config_manager import ConfigProvider
from web_driver.chrome_driver import ChromeDriver


@pytest.fixture(scope="function")
def driver():
    driver = ChromeDriver().get_driver()
    driver.set_window_size(
        ConfigProvider().instance().driver_window_width,
        ConfigProvider().instance().driver_window_height
    )
    driver.implicitly_wait(ConfigProvider().instance().driver_implicitly_wait)
    yield driver
    driver.quit()