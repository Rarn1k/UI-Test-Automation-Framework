from abc import ABC, abstractmethod


class BasePage(ABC):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        self._locator = locator
        self._name = name

    @abstractmethod
    def is_displayed(self) -> bool:
        pass