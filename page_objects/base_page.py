from element_objects.label import Label
from utils.logger_manager import LoggerManager


class BasePage:
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        self._locator = locator
        self._name = name

    def is_displayed(self) -> bool:
        LoggerManager().info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()