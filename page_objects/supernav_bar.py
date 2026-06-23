from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SupernavBar(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._root = self._bot.element(self._main_by)
        self._about_by = By.XPATH, ".//a[contains(@href, 'about')]"
        self._store_by = By.XPATH, ".//a[contains(@data-tooltip-content, 'Store')]"

    @property
    def _main_by(self) -> tuple:
        return By.CLASS_NAME, "supernav_container"

    def click_about(self) -> "AboutPage":
        from page_objects.about_page import AboutPage
        self._bot.click(self._about_by, self._root)
        return AboutPage(self._driver)

    def click_store(self) -> "HomePage":
        from page_objects.home_page import HomePage
        self._bot.click(self._store_by, self._root)
        return HomePage(self._driver)