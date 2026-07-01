from selenium.webdriver.common.by import By

from element_objects.href import Href
from page_objects.base_page import BasePage
from utils.config.config_manager import ConfigManager
from web_driver.driver_factory import DriverFactory


class MainPage(BasePage):
    def __init__(self) -> None:
        super().__init__((By.CLASS_NAME, "home-banner"), "Main Page")
        self.url = ConfigManager().instance().demoqa_url

    def is_displayed(self) -> bool:
        return Href(self._locator, self._name).find_element().is_displayed()

    def load_page(self) -> None:
        DriverFactory.create_driver().get_driver().get(self.url)