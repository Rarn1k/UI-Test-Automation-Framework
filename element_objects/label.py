from selenium.webdriver.remote.webelement import WebElement

from element_objects.base_element import BaseElement
from utils.logger_manager import LoggerManager


class Label(BaseElement):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        super().__init__(locator, name)

    def wait_closed(self) -> bool:
        LoggerManager().info(f"Ждём, пока label '{self._name}' закроется")
        return self._waiter.wait_for_invisibility(self._locator)

    def get_texts(self, parent : WebElement | None = None) -> list[str]:
        labels = self.find_elements(parent)
        LoggerManager().info(f"Возвращаем тексты элементов: '{self._name}'")
        return [label.text.strip() for label in labels]
