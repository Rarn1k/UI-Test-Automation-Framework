from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SupernavBar(BasePage):
    _about_by = By.XPATH, ".//a[contains(@href, 'about')]"
    _store_by = By.XPATH, ".//a[contains(@data-tooltip-content, 'Store')]"

    def __init__(self, driver):
        super().__init__(driver)
        self._root = self._bot.element(self._main_by)

    @property
    def _main_by(self) -> tuple:
        return By.CLASS_NAME, "supernav_container"

    def click_about(self) -> None:
        self._bot.click(self._about_by, self._root)

    def click_store(self) -> None:
        self._bot.click(self._store_by, self._root)
