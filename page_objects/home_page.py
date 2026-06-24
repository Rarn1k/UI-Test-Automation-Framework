from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utils.config.config_manager import ConfigProvider


class HomePage(BasePage):
    URL = ConfigProvider().instance().steam_url

    _top_sellers_by = By.ID, "tab_topsellers_content_trigger"

    @property
    def _main_by(self):
        return By.CLASS_NAME, "home_page_body_ctn"

    def load_page(self) -> None:
        self._driver.get(self.URL)

    def click_top_sellers(self) -> None:
        self._bot.click(self._top_sellers_by)

    def is_top_sellers_active(self) -> bool:
        top_sellers = self._bot.element(self._top_sellers_by)
        return top_sellers.get_attribute("aria-selected") == "true"