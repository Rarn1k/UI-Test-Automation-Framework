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

    def _get_wait(self, context=None) -> WebDriverWait:
        return WebDriverWait(
            driver=context or Driver().get_driver(),
            timeout=self._timeout,
        )

    def _until(self, condition: Callable, message: str = "", context=None) -> T:
        try:
            logger.info(f"Ждём пока выполнится условие: {condition}")
            result = self._get_wait(context).until(condition)
            return result
        except TimeoutException as e:
            logger.error(f"Таймаут ожидания: {message or e}")
            raise

    def wait_for_presence(self, locator: tuple[str, str], parent: WebElement | None = None) -> WebElement:
        return self._until(
            lambda context: context.find_element(*locator),
            f"Не удалось найти элемент по локатору {locator}",
            parent
        )

    def wait_for_all_present(self, locator: tuple[str, str], parent: WebElement | None = None) -> list[WebElement]:
        return self._until(
            lambda context: context.find_elements(*locator),
            f"Не удалось найти элементы по локатору {locator}",
            parent
        )

    def wait_for_clickable(self, locator: tuple[str, str]) -> WebElement:
        return self._until(EC.element_to_be_clickable(locator), f"Элемент {locator} не стал кликабельным")

    def wait_for_alert(self) -> Alert:
        return self._until(EC.alert_is_present(), "Алерт не появился")

    def wait_until_alert_closed(self) -> bool:
        def alert_is_not_present(driver: WebDriver) -> bool:
            try:
                driver.switch_to.alert
                return False
            except NoAlertPresentException:
                return True

        return self._until(alert_is_not_present)

    def wait_for_invisibility(self, locator: tuple[str, str]) -> bool:
        return self._until(EC.invisibility_of_element_located(locator), f"Элемент {locator} не исчез")

    def wait_for_new_window(self, old_handles: list[str]) -> bool:
        return self._until(
            lambda d: len(d.window_handles) > len(old_handles),
            "Новая вкладка не появилась за отведённое время"
        )

    def wait_for_url_not_blank(self) -> None:
        self._until(
            lambda d: d.current_url != "about:blank",
            "Ссылка осталась пустой"
        )

    def wait_to_switch_frame(self, frame: WebElement) -> None:
        self._until(EC.frame_to_be_available_and_switch_to_it(frame))