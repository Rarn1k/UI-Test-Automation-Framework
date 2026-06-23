from selenium.common import (
    NoSuchElementException,
    StaleElementReferenceException,
    ElementNotInteractableException,
)
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from utils.config.config_manager import ConfigProvider


class ActionBot:
    def __init__(self, driver) -> None:
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

    def click(self, locator: tuple, parent: WebElement = None) -> None:
        element = self.element(locator, parent)
        element.click()
