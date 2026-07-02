from selenium.webdriver.remote.webdriver import WebDriver
from utils.singleton_meta import SingletonMeta
from web_driver.driver_factory import DriverFactory

import logging

logger = logging.getLogger(__name__)

class Driver(metaclass=SingletonMeta):
    def __init__(self):
        logger.debug("Создаём экземпляр обёртки Driver")
        self._wrapper = DriverFactory.create_driver()

    def get_driver(self) -> WebDriver:
        return self._wrapper.get_driver()

    def quit(self) -> None:
        if self._wrapper:
            logger.debug("Обёртка Driver вызывает завершение драйвера")
            self._wrapper.quit()
            self._wrapper = None
            logger.debug("Удаляем экземпляр обёртки")
            type(self).clear_instance()
