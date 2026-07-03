import logging

from element_objects.base_element import BaseElement

logger = logging.getLogger(__name__)


class Input(BaseElement):
    def __init__(self, locator: tuple[str, str], name: str):
        super().__init__(locator, name)

    def set_value(self, text: str) -> None:
        logger.info(f"Ввод текста '{text}' в поле '{self._name}'")
        element = self._waiter.wait_for_clickable(self._locator)
        element.clear()
        element.send_keys(text)
