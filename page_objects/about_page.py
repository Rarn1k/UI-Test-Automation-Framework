from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from page_objects.action_bot import ActionBot
from page_objects.loadable_component import LoadableComponent


class AboutPage(LoadableComponent):
    URL = "https://store.steampowered.com/about/"  # В конфиг

    _main_by = By.ID, "about_header_area"
    def __init__(self, driver):
        self._driver = driver
        self._bot = ActionBot(driver)

    def load(self) -> None:
        self._driver.get(self.URL)

    def is_loaded(self) -> bool:
        try:
            WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located(self._main_by)
            )
            return True
        except TimeoutException:
            return False
