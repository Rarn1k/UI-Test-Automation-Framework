from selenium.webdriver.common.by import By

from page_objects.about_page import AboutPage
from page_objects.base_page import BasePage


class SupernavBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._root = self._bot.element(self._main_by)
        self._about_by = By.XPATH, ".//a[contains(@href, 'about')]"

    @property
    def _main_by(self) -> tuple:
        return By.CLASS_NAME, "supernav_container"

    def click_about(self) -> AboutPage:
        self._bot.click(self._about_by, self._root)
        return AboutPage(self._driver)
