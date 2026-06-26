from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class TopSellersPage(BasePage):
    _more_top_sellers_by = By.XPATH, "//button[contains(text(), 'Browse More Top Sellers')]"
    @property
    def _main_by(self) -> tuple[str, str]:
        return By.XPATH, "//*[contains(@class, 'SteamChartsShell')]"

    def click_more_top_sellers(self) -> None:
        self._bot.click(self._more_top_sellers_by)