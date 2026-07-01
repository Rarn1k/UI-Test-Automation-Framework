from abc import ABC, abstractmethod


class BasePage(ABC):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        self.__locator = locator
        self.__name = name

    @abstractmethod
    def is_displayed(self) -> bool:
        pass