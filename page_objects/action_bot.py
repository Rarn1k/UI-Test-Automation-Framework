from typing import Callable

from selenium.common import (
    NoSuchElementException,
    StaleElementReferenceException,
    ElementNotInteractableException,
)
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from selenium import webdriver
from utils.config.config_manager import ConfigProvider


class ActionBot:
    def __init__(self, driver: webdriver) -> None:
        self._driver = driver
        self._wait = WebDriverWait(
            driver,
            timeout=ConfigProvider().instance().timeout,
            ignored_exceptions=[
                NoSuchElementException,
                StaleElementReferenceException,
                ElementNotInteractableException,
            ],
        )

    def element(self, locator: tuple, parent: WebElement = None) -> WebElement:
        context = parent if parent is not None else self._driver
        return self._wait.until(lambda _: context.find_element(*locator))

    def elements(self, locator: tuple) -> list[WebElement]:
        return self._driver.find_elements(*locator)

    def click(self, locator: tuple, parent: WebElement = None) -> None:
        element = self.element(locator, parent)
        element.click()

    def text(self, locator: tuple) -> str:
        element = self.element(locator)
        return element.text

    def wait_until(self, condition: Callable) -> None:
        self._wait.until(condition)
