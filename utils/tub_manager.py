from urllib.parse import urlparse

from utils.waiter import Waiter
from web_driver.driver import Driver
import logging

logger = logging.getLogger(__name__)


class TubManager:
    def __init__(self) -> None:
        self._waiter = Waiter()

    @staticmethod
    def get_all_handles() -> list[str]:
        logger.info("Получаем все вкладки")
        return Driver().get_driver().window_handles

    @staticmethod
    def get_current_handle() -> str:
        logger.info("Получаем текущую вкладку")
        return Driver().get_driver().current_window_handle

    def get_current_url(self) -> str:
        logger.info("Получаем URL текущей вкладки")
        self._waiter.wait_for_url_not_blank()
        return Driver().get_driver().current_url

    def get_current_path(self) -> str:
        logger.info("Получаем путь текущей вкладки")
        full_url = self.get_current_url()
        parsed = urlparse(full_url)
        path = parsed.path or "/"
        return path

    def get_new_window_opened(self, old_handles: list[str]) -> str:
        self._waiter.wait_for_new_window(old_handles)
        logger.info("Получаем новую вкладку")
        new_handles = self.get_all_handles()
        new_handle = (set(new_handles) - set(old_handles)).pop()
        return new_handle

    @staticmethod
    def switch_to_window(handle: str) -> None:
        logger.info(f"Переключаемся на вкладку с handle: {handle}")
        Driver().get_driver().switch_to.window(handle)

    def switch_to_new_window(self, old_handles: list[str]) -> str:
        new_handle = self.get_new_window_opened(old_handles)
        self.switch_to_window(new_handle)
        return new_handle

    @staticmethod
    def close_current_window() -> None:
        logger.info("Закрываем текущую вкладку")
        Driver().get_driver().close()
