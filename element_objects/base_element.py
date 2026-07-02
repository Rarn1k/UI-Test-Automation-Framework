from abc import ABC

from selenium.webdriver.remote.webelement import WebElement

from utils.waiter import Waiter

import logging
logger = logging.getLogger(__name__)

class BaseElement(ABC):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        self._locator = locator
        self._name = name
        self._waiter = Waiter()

    def find_element(self) -> WebElement:
        logger.info(f"Ищем элемент {self._name} по локатору {self._locator}")
        return self._waiter.wait_for_presence(self._locator)

    def click(self) -> None:
        logger.info(f"Нажимаем на элемент {self._name}")
        element = self._waiter.wait_for_clickable(self._locator)
        element.click()
