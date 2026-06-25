from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from utils.text_handler import TextHandler


class AboutPage(BasePage):
    _gamers_online_by = By.XPATH, "//*[contains(*//@class, 'gamers_online')]"
    _gamers_in_game = By.XPATH, "//*[contains(*//@class, 'gamers_in_game')]"

    @property
    def _main_by(self):
        return By.ID, "about_header_area"

    def get_gamers_online(self) -> int:
        text = self._bot.text(self._gamers_online_by)
        return TextHandler.get_num_from_text(text)

    def get_gamers_in_game(self) -> int:
        text = self._bot.text(self._gamers_in_game)
        return TextHandler.get_num_from_text(text)
