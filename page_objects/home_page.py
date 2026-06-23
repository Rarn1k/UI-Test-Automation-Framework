from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.supernav_bar import SupernavBar
from utils.config.config_manager import ConfigProvider


class HomePage(BasePage):
    URL = ConfigProvider().instance().steam_url

    @property
    def _main_by(self):
        return By.CLASS_NAME, "home_page_body_ctn"

    def load_page(self) -> None:
        self._driver.get(self.URL)

    def get_supernav_bar(self) -> SupernavBar:
        return SupernavBar(self._driver)
