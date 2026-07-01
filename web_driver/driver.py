from selenium.webdriver.remote.webdriver import WebDriver
from utils.singleton_meta import SingletonMeta
from web_driver.driver_factory import DriverFactory

class Driver(metaclass=SingletonMeta):
    def __init__(self):
        self._wrapper = DriverFactory.create_driver()

    def get_driver(self) -> WebDriver:
        return self._wrapper.get_driver()

    def quit(self) -> None:
        if self._wrapper:
            self._wrapper.quit()
