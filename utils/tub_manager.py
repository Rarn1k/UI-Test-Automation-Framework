from urllib.parse import urlparse

from utils.logger_manager import LoggerManager
from utils.waiter import Waiter
from web_driver.driver import Driver



class TubManager:
    @staticmethod
    def get_all_handles() -> list[str]:
        LoggerManager().info("Получаем все вкладки")
        return Driver().get_driver().window_handles

    @staticmethod
    def get_current_handle() -> str:
        LoggerManager().info("Получаем текущую вкладку")
        return Driver().get_driver().current_window_handle

    @staticmethod
    def get_current_url() -> str:
        LoggerManager().info("Получаем URL текущей вкладки")
        Waiter.wait_for_url_not_blank()
        return Driver().get_driver().current_url

    def get_current_path(self) -> str:
        LoggerManager().info("Получаем путь текущей вкладки")
        full_url = self.get_current_url()
        parsed = urlparse(full_url)
        path = parsed.path or "/"
        return path

    def get_new_window_opened(self, old_handles: list[str]) -> str:
        Waiter.wait_for_new_window(old_handles)
        LoggerManager().info("Получаем новую вкладку")
        new_handles = self.get_all_handles()
        new_handle = (set(new_handles) - set(old_handles)).pop()
        return new_handle

    @staticmethod
    def switch_to_window(handle: str) -> None:
        LoggerManager().info(f"Переключаемся на вкладку с handle: {handle}")
        Driver().get_driver().switch_to.window(handle)

    def switch_to_new_window(self, old_handles: list[str]) -> str:
        new_handle = self.get_new_window_opened(old_handles)
        self.switch_to_window(new_handle)
        return new_handle

    @staticmethod
    def close_current_window() -> None:
        LoggerManager().info("Закрываем текущую вкладку")
        Driver().get_driver().close()

    def get_previous_window(self) -> str:
        LoggerManager().info("Переключаемся на предыдущую вкладку")
        handles = self.get_all_handles()
        if len(handles) < 2:
            raise RuntimeError("Нет предыдущей вкладки для переключения")
        current_handle = self.get_current_handle()
        for i in range(1, len(handles)):
            if handles[i] == current_handle:
                return handles[i - 1]
        raise RuntimeError("Не удалось найти предыдущую вкладку")

    def switch_to_previous_window(self) -> None:
        handle = self.get_previous_window()
        self.switch_to_window(handle)