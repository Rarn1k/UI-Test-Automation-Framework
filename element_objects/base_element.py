from abc import ABC

from selenium.common import TimeoutException
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from utils.config.config_manager import ConfigManager
from web_driver.driver import Driver

import logging
logger = logging.getLogger(__name__)

class BaseElement(ABC):
    def __init__(self, locator: tuple[str, str], name: str) -> None:
        self._locator = locator
        self._name = name

    def find_element(self) -> WebElement:
        logger.info(f"Ищем элемент {self._name} по локатору {self._locator}")
        try:
            element = WebDriverWait(
                driver=Driver().get_driver(), timeout=ConfigManager().instance().timeout
            ).until(EC.presence_of_element_located(self._locator))
            return element
        except TimeoutException:
            logger.error(f"Элемент '{self._name}' не найден по локатору {self._locator}")
            raise

    def click(self) -> None:
        logger.info(f"Нажимаем на элемент {self._name}")
        try:
            element = WebDriverWait(
                driver=Driver().get_driver(), timeout=ConfigManager().instance().timeout
            ).until(EC.element_to_be_clickable(self._locator))
            element.click()
        except TimeoutException:
            logger.error(f"Элемент '{self._name}' не стал кликабельным")
            raise
