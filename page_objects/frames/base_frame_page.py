from abc import ABC, abstractmethod

from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page import BasePage
from web_driver.driver import Driver


class BaseFramePage(BasePage, ABC):
    def __init__(self, locator: tuple[str, str], name: str):
        super().__init__(locator, name)

    @abstractmethod
    def _get_this_frame(self) -> WebElement:
        pass

    def switch_to_this_frame(self) -> None:
        Driver().get_driver().switch_to.frame(self._get_this_frame())

    @staticmethod
    def switch_to_default() -> None:
        Driver().get_driver().switch_to.default_content()