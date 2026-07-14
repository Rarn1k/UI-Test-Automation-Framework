from abc import ABC

from selenium.webdriver.remote.webdriver import WebDriver

from utils.logger_manager import LoggerManager
from utils.singleton_meta import SingletonMeta


class BaseDriver(ABC, metaclass=SingletonMeta):
    def __init__(self) -> None:
        LoggerManager().debug("Инициализируем драйвер")
        self._driver = None

    def get_driver(self) -> WebDriver:
        if self._driver is None:
            LoggerManager().error("Драйвер не инициализирован, но была попытка его получить")
            raise RuntimeError("Драйвер не инициализирован. Сначала вызовите метод инициализации.")
        LoggerManager().debug(f"Возвращаем драйвер {self._driver}")
        return self._driver

    def quit(self) -> None:
        if self._driver:
            LoggerManager().debug("Закрываем драйвер")
            self._driver.quit()
            self._driver = None
            LoggerManager().info("Удаляем экземпляр драйвера")
            type(self).clear_instance()

    def load_page(self, url: str) -> None:
        if self._driver:
            LoggerManager().info(f"Драйвер загружает страницу {url}")
            self._driver.get(url)
