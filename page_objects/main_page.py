from selenium.webdriver.common.by import By

from element_objects.href import Href
from page_objects.base_page import BasePage
from utils.config.config_manager import ConfigManager
from web_driver.driver_factory import DriverFactory

import logging
logger = logging.getLogger(__name__)

class MainPage(BasePage):
    __alerts_href = Href((By.XPATH, "//a[@href='/alertsWindows']"), "alerts link")

    def __init__(self) -> None:
        super().__init__((By.CLASS_NAME, "home-banner"), "Main Page")
        self.url = ConfigManager().instance().demoqa_url

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Href(self._locator, self._name).find_element().is_displayed()

    def load_page(self) -> None:
        logger.info(f"Загружаем страницу {self._name}")
        DriverFactory.create_driver().get_driver().get(self.url)

    def click_alerts_windows(self) -> None:
        self.__alerts_href.find_and_click()