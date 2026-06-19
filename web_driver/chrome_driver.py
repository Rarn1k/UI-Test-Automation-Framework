from selenium import webdriver

from web_driver.singleton_meta import SingletonMeta


class ChromeDriver(metaclass=SingletonMeta):
    def __init__(self):
        options = self._get_default_chrome_options()
        options.add_argument("--incognito")
        self.driver = webdriver.Chrome(options=options)

    def get_driver(self):
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()
            SingletonMeta._instances.pop(self.__class__, None)

    @staticmethod
    def _get_default_chrome_options():
        options = webdriver.ChromeOptions()
        options.add_argument("--no-sandbox")
        return options
