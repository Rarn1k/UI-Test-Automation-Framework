from selenium import webdriver

from web_driver.base_driver import BaseDriver


class ChromeDriver(BaseDriver):
    def __init__(self) -> None:
        super().__init__()
        options = self._set_options()
        self._driver = webdriver.Chrome(options=options)

    def _get_options(self) -> webdriver.ChromeOptions:
        return webdriver.ChromeOptions()
