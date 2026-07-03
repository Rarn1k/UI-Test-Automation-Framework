import logging

from element_objects.base_element import BaseElement

logger = logging.getLogger(__name__)


class Label(BaseElement):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        super().__init__(locator, name)

    def wait_closed(self) -> bool:
        logger.info(f"Ждём, пока label '{self._name}' закроется")
        return self._waiter.wait_for_invisibility(self._locator)
