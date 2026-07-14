from abc import ABC

from selenium.common import ElementClickInterceptedException
from selenium.webdriver.remote.webelement import WebElement

from utils.logger_manager import LoggerManager
from utils.waiter import Waiter

from web_driver.driver import Driver


class BaseElement(ABC):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        self._locator = locator
        self._name = name
        self._waiter = Waiter()

    def find_element(self, parent: WebElement | None = None) -> WebElement:
        context = parent if parent else "всей страницы"
        LoggerManager().info(f"Ищем элемент {self._name} по локатору {self._locator} внутри {context}")
        return self._waiter.wait_for_presence(self._locator, parent)

    def find_elements(self, parent: WebElement | None = None) -> list[WebElement]:
        context = parent if parent else "всей страницы"
        LoggerManager().info(f"Ищем элементы {self._name} по локатору {self._locator} внутри {context}")
        return self._waiter.wait_for_all_present(self._locator, parent)

    def click(self) -> None:
        LoggerManager().info(f"Нажимаем на элемент {self._name}")
        element = self._waiter.wait_for_clickable(self._locator)
        try:
            element.click()
        except ElementClickInterceptedException:
            Driver().get_driver().execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
            element = self._waiter.wait_for_clickable(self._locator)
            element.click()
