from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utils.text_handler import TextHandler


class GamePage(BasePage):
    _title_by = By.ID, "appHubAppName"
    _release_by = By.XPATH, "//*[contains(@class, 'release_date')]//*[contains(@class, 'date')]"
    _price_by = By.XPATH, "(//*[contains(@class, 'discount_final_price') or contains(@class, 'game_purchase_price')])[1]"

    @property
    def _main_by(self) -> tuple:
        return By.XPATH, "//*[contains(@class, 'game_bg')]"

    def get_title(self) -> str:
        return self._bot.element(self._title_by).text

    def get_release(self):
        return self._bot.element(self._release_by).text

    def get_price(self):
        text = self._bot.element(self._price_by).text
        return TextHandler.get_num_from_text(text)