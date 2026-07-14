from element_objects.base_element import BaseElement
from element_objects.label import Label
from utils.logger_manager import LoggerManager


class BasePage:
    def __init__(self, element: BaseElement | Label, name: str) -> None:
        self._element = element
        self._name = name

    def is_displayed(self) -> bool:
        LoggerManager().info(f"Проверяем, загружена ли страница {self._name}")
        return self._element.find_element().is_displayed()