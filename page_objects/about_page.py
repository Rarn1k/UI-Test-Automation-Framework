from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage
from page_objects.supernav_bar import SupernavBar


class AboutPage(BasePage):
    _gamers_online_by = By.XPATH, "//*[contains(*//@class, 'gamers_online')]"
    _gamers_in_game = By.XPATH, "//*[contains(*//@class, 'gamers_in_game')]"

    @property
    def _main_by(self):
        return By.ID, "about_header_area"

    def get_gamers_online(self) -> int:
        text = self._bot.text(self._gamers_online_by)
        nums = text.split('\n')[-1]
        return int(nums.replace(",", ""))

    def get_gamers_in_game(self) -> int:
        text = self._bot.text(self._gamers_in_game)
        nums = text.split('\n')[-1]
        return int(nums.replace(",", ""))

    def get_supernav_bar(self) -> SupernavBar:
        return SupernavBar(self._driver)