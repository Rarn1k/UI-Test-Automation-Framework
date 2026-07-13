from element_objects.base_element import BaseElement
from utils.logger_manager import LoggerManager


class Input(BaseElement):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        super().__init__(locator, name)

    def set_value(self, text: str) -> None:
        LoggerManager().get_logger().info(f"Ввод текста '{text}' в поле '{self._name}'")
        element = self._waiter.wait_for_presence(self._locator)
        element.clear()
        element.send_keys(text)
