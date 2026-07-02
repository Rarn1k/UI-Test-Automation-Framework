from typing import Callable, TypeVar

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

from utils.config.config_manager import ConfigManager

import logging

from web_driver.driver import Driver

logger = logging.getLogger(__name__)

T = TypeVar("T")


class Waiter:
    def __init__(self):
        self._timeout = ConfigManager().instance().timeout

    @property
    def _wait(self):
        return WebDriverWait(
            driver=Driver().get_driver(),
            timeout=self._timeout,
        )

    def until(self, condition: Callable, message: str = "") -> T:
        try:
            logger.info(f"Ждём пока выполнится условие: {condition}")
            result = self._wait.until(condition)
            return result
        except TimeoutException as e:
            logger.error(f"Таймаут ожидания: {message or e}")
            raise

    def wait_for_presence(self, locator: tuple[str, str]) -> WebElement:
        return self.until(EC.presence_of_element_located(locator), f"Элемент {locator} не появился в DOM")

    def wait_for_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self.until(EC.element_to_be_clickable(locator), f"Элемент {locator} не стал кликабельным")

    def wait_for_alert(self) -> Alert:
        return self.until(EC.alert_is_present(), "Алерт не появился")

    def wait_until_alert_closed(self) -> bool:
        def alert_is_not_present(driver: WebDriver) -> bool:
            try:
                driver.switch_to.alert
                return False
            except NoAlertPresentException:
                return True

        return self._wait.until(alert_is_not_present)