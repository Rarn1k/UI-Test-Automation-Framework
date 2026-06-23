from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from page_objects.action_bot import ActionBot


class AboutPage:
    _main_by = By.ID, "about_header_area"

    def __init__(self, driver):
        self._driver = driver
        self._bot = ActionBot(driver)

    def is_loaded(self) -> bool:
        try:
            self._bot.element(self._main_by)
            return True
        except TimeoutException:
            return False
