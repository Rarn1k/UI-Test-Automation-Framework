from abc import ABC

from selenium.webdriver.remote.webelement import WebElement
from web_driver.driver import Driver


class BaseElement(ABC):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        self.__locator = locator
        self.__name = name

    def find_element(self) -> WebElement:
        return Driver().get_driver().find_element(*self.__locator)

    @staticmethod
    def click(element: WebElement) -> None:
        element.click()

    def find_and_click(self) -> None:
        self.click(self.find_element())