from selenium import webdriver

from utils.config.config_manager import ConfigProvider
from utils.singleton_meta import SingletonMeta


class ChromeDriver(metaclass=SingletonMeta):
    def __init__(self):
        options = self._set_chrome_options()
        self.driver = webdriver.Chrome(options=options)

    def get_driver(self):
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()

    @staticmethod
    def _set_chrome_options():
        options = webdriver.ChromeOptions()
        for arg in ConfigProvider().instance().driver_args:
            options.add_argument(arg)
        return options
