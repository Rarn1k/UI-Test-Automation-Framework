from abc import ABC, abstractmethod

from selenium.webdriver.common.options import ArgOptions

from selenium.webdriver.remote.webdriver import WebDriver

from utils.config.config_manager import ConfigManager
from utils.singleton_meta import SingletonMeta


class BaseDriver(ABC, metaclass=SingletonMeta):
    def __init__(self) -> None:
        self._driver = None

    def get_driver(self) -> WebDriver:
        return self._driver

    def quit(self) -> None:
        if self._driver:
            self._driver.quit()
            self._driver = None
            type(self).clear_instance()

    @abstractmethod
    def _get_options(self) -> ArgOptions:
        pass

    def _set_options(self) -> ArgOptions:
        options = self._get_options()
        for arg in ConfigManager().instance().driver_args:
            options.add_argument(arg)
        return options
