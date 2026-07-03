import time
from abc import ABC

from selenium.webdriver.remote.webdriver import WebDriver

from utils.singleton_meta import SingletonMeta

import logging

logger = logging.getLogger(__name__)


class BaseDriver(ABC, metaclass=SingletonMeta):
    def __init__(self) -> None:
        logger.debug("Инициализируем драйвер")
        self._driver = None

    def get_driver(self) -> WebDriver:
        logger.debug(f"Возвращаем драйвер {self._driver}")
        return self._driver

    def quit(self) -> None:
        if self._driver:
            logger.debug("Закрываем драйвер")
            self._driver.quit()
            self._driver = None
            logger.info("Удаляем экземпляр драйвера")
            type(self).clear_instance()

    def load_page(self, url: str) -> None:
        if self._driver:
            logger.info(f"Драйвер загружает страницу {url}")
            self._driver.get(url)
