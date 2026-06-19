from selenium import webdriver

from web_driver.singleton_meta import SingletonMeta


class ChromeDriver(metaclass=SingletonMeta):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def get_driver(self):
        return self.driver

    def quit(self):
        if self.driver:
            self.driver.quit()
