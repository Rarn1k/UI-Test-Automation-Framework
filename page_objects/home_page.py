from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from page_objects.about_page import AboutPage
from page_objects.action_bot import ActionBot
from page_objects.base_page import BasePage
from page_objects.supernav_bar import SupernavBar
from utils.config.config_manager import ConfigProvider


class HomePage(BasePage):
    URL = ConfigProvider().instance().steam_url

    _about_by = By.XPATH, "//*[contains(@class, 'supernav')]//a[contains(@href, 'about')]"

    @property
    def _main_by(self):
        return By.CLASS_NAME, "home_page_body_ctn"

    def load_page(self) -> None:
        self._driver.get(self.URL)

    def click_about(self) -> AboutPage:
        self._bot.click(self._about_by)
        return AboutPage(self._driver)
