from abc import ABC, abstractmethod

from selenium import webdriver
from selenium.common import TimeoutException

from page_objects.action_bot import ActionBot


class BasePage(ABC):
    def __init__(self, driver: webdriver) -> None:
        self._driver = driver
        self._bot = ActionBot(driver)

    @property
    @abstractmethod
    def _main_by(self) -> tuple[str, str]:
        pass

    def is_loaded(self) -> bool:
        try:
            self._bot.element(self._main_by)
            return True
        except TimeoutException:
            return False
