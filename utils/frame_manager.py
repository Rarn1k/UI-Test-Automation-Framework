import logging

from selenium.webdriver.remote.webelement import WebElement

from web_driver.driver import Driver

logger = logging.getLogger(__name__)


class FrameManager:
    @staticmethod
    def switch_to_frame(frame: WebElement) -> None:
        logger.info(f"Переключаемся на фрейм {frame}")
        Driver().get_driver().switch_to.frame(frame)

    @staticmethod
    def switch_to_default() -> None:
        logger.info(f"Переключаемся на обычную страницу")
        Driver().get_driver().switch_to.default_content()
