from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions

from utils.config.config_manager import ConfigManager
from utils.logger_manager import LoggerManager
from web_driver.base_driver import BaseDriver


class FirefoxDriver(BaseDriver):
    def __init__(self) -> None:
        super().__init__()
        options = self._set_options()
        LoggerManager().info("Создаём драйвер Firefox")
        self._driver = webdriver.Firefox(options=options)

    @staticmethod
    def _set_options() -> ArgOptions:
        options = webdriver.FirefoxOptions()
        for arg in ConfigManager().instance().firefox_driver_args:
            options.add_argument(arg)
        return options
