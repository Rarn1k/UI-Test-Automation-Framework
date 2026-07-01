from abc import ABC

from selenium.webdriver.remote.webdriver import WebDriver

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
