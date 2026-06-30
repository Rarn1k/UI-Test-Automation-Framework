from selenium import webdriver

from web_driver.base_driver import BaseDriver


class FirefoxDriver(BaseDriver):
    def __init__(self) -> None:
        super().__init__()
        options = self._set_options()
        self._driver = webdriver.Firefox(options=options)

    def _get_options(self) -> webdriver.FirefoxOptions:
        return webdriver.FirefoxOptions()
