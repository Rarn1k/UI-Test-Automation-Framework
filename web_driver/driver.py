from selenium.webdriver.remote.webdriver import WebDriver

from utils.logger_manager import LoggerManager
from utils.singleton_meta import SingletonMeta
from web_driver.driver_factory import DriverFactory


class Driver(metaclass=SingletonMeta):
    def __init__(self):
        LoggerManager().get_logger().debug("Создаём экземпляр обёртки Driver")
        self._wrapper = DriverFactory.create_driver()

    def get_driver(self) -> WebDriver:
        return self._wrapper.get_driver()

    def quit(self) -> None:
        if self._wrapper:
            LoggerManager().get_logger().debug("Обёртка Driver вызывает завершение драйвера")
            self._wrapper.quit()
            self._wrapper = None
            LoggerManager().get_logger().debug("Удаляем экземпляр обёртки")
            type(self).clear_instance()

    def load_page(self, url: str) -> None:
        if self._wrapper:
            LoggerManager().get_logger().info(f"Загружаем страницу с обёртки {url}")
            self._wrapper.load_page(url)
