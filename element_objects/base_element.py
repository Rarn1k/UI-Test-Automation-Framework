from abc import ABC

from selenium.webdriver.remote.webelement import WebElement
from web_driver.driver import Driver

import logging
logger = logging.getLogger(__name__)

class BaseElement(ABC):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        self._locator = locator
        self._name = name

    def find_element(self) -> WebElement:
        logger.info(f"Ищем элемент {self._name} по локатору {self._locator}")
        return Driver().get_driver().find_element(*self._locator)

    @staticmethod
    def click(element: WebElement) -> None:
        logger.info(f"Нажимаем на элемент {element}")
        element.click()

    def find_and_click(self) -> None:
        self.click(self.find_element())