from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class NavBar(BasePage):
    _browse_by = By.XPATH, ".//*[(text()='Browse')]"
    _top_sellers_by = By.XPATH, ".//*[contains(text(), 'Top Sellers')]"

    def __init__(self, driver) -> None:
        super().__init__(driver)
        self._root = self._bot.element(self._main_by)

    @property
    def _main_by(self) -> tuple[str, str]:
        return By.XPATH, "//*[contains(@aria-label, 'menu')]/parent::*"

    def click_browse(self) -> None:
        self._bot.click(self._browse_by, self._root)

    def click_top_sellers(self) -> None:
        self._bot.click(self._top_sellers_by, self._root)