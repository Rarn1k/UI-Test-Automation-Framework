from typing import Callable, TypeVar

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoAlertPresentException

from utils.config.config_manager import ConfigManager

from utils.logger_manager import LoggerManager
from web_driver.driver import Driver

T = TypeVar("T")


class Waiter:
    @staticmethod
    def _get_wait(context=None) -> WebDriverWait:
        return WebDriverWait(
            driver=context or Driver().get_driver(),
            timeout=ConfigManager().instance().timeout,
        )

    @classmethod
    def _until(cls, condition: Callable, message: str = "", context=None) -> T:
        try:
            LoggerManager().info(f"Ждём пока выполнится условие: {condition}")
            result = cls._get_wait(context).until(condition)
            return result
        except TimeoutException as e:
            LoggerManager().error(f"Таймаут ожидания: {message or e}")
            raise

    @classmethod
    def wait_for_presence(cls, locator: tuple[str, str], parent: WebElement | None = None) -> WebElement:
        return cls._until(
            lambda context: context.find_element(*locator),
            f"Не удалось найти элемент по локатору {locator}",
            parent
        )

    @classmethod
    def wait_for_all_present(cls, locator: tuple[str, str], parent: WebElement | None = None) -> list[WebElement]:
        return cls._until(
            lambda context: context.find_elements(*locator),
            f"Не удалось найти элементы по локатору {locator}",
            parent
        )

    @classmethod
    def wait_for_clickable(cls, locator: tuple[str, str]) -> WebElement:
        return cls._until(EC.element_to_be_clickable(locator), f"Элемент {locator} не стал кликабельным")

    @classmethod
    def wait_for_alert(cls) -> Alert:
        return cls._until(EC.alert_is_present(), "Алерт не появился")

    @classmethod
    def wait_until_alert_closed(cls) -> bool:
        def alert_is_not_present(driver: WebDriver) -> bool:
            try:
                driver.switch_to.alert
                return False
            except NoAlertPresentException:
                return True

        return cls._until(alert_is_not_present)

    @classmethod
    def wait_for_invisibility(cls, locator: tuple[str, str]) -> bool:
        return cls._until(EC.invisibility_of_element_located(locator), f"Элемент {locator} не исчез")

    @classmethod
    def wait_for_next_window(cls, windows_count: int) -> bool:
        return cls._until(
            lambda d: len(d.window_handles) > windows_count,
            "Новая вкладка не появилась за отведённое время"
        )

    @classmethod
    def wait_for_url_not_blank(cls) -> None:
        cls._until(
            lambda d: d.current_url != "about:blank",
            "Ссылка осталась пустой"
        )

    @classmethod
    def wait_to_switch_frame(cls, frame: WebElement) -> None:
        cls._until(EC.frame_to_be_available_and_switch_to_it(frame))
