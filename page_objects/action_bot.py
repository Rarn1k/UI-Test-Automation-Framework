from selenium.common import (
    NoSuchElementException,
    StaleElementReferenceException,
    ElementNotInteractableException,
)
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class ActionBot:
    def __init__(self, driver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(
            driver,
            timeout=10,  # В конфиг
            ignored_exceptions=[
                NoSuchElementException,
                StaleElementReferenceException,
                ElementNotInteractableException,
            ],
        )

    def element(self, locator: tuple) -> WebElement:
        self.wait.until(lambda driver: driver.find_element(*locator))
        return self.driver.find_element(*locator)

    def click(self, locator: tuple) -> None:
        element = self.element(locator)
        element.click()
