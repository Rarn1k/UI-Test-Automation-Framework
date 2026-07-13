from collections.abc import Generator
from contextlib import contextmanager
from typing import Any

from selenium.webdriver.remote.webdriver import WebDriver

from element_objects.base_element import BaseElement
from utils.logger_manager import LoggerManager
from utils.waiter import Waiter
from web_driver.driver import Driver



class FrameManager:

    @staticmethod
    def switch_to_frame(element: BaseElement) -> None:
        LoggerManager().get_logger().info(f"Переключаемся на фрейм по элементу {element}")
        frame = element.find_element()
        Waiter().wait_to_switch_frame(frame)

    @staticmethod
    def switch_to_default() -> None:
        LoggerManager().get_logger().info(f"Переключаемся на обычную страницу")
        Driver().get_driver().switch_to.default_content()

    @classmethod
    @contextmanager
    def frame_context(cls, element: BaseElement) -> Generator[WebDriver, Any, None]:
        cls.switch_to_frame(element)
        try:
            yield Driver().get_driver()
        finally:
            cls.switch_to_default()
