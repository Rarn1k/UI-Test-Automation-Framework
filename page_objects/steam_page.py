from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from page_objects.loadable_component import LoadableComponent


class SteamPage(LoadableComponent):
    URL = "https://store.steampowered.com"  # В конфиг

    def __init__(self, driver):
        self._driver = driver

    def _load(self) -> None:
        self._driver.get(self.URL)

    def _is_loaded(self) -> bool:
        try:
            WebDriverWait(self._driver, 10).until(
                EC.visibility_of_element_located(
                    (By.CLASS_NAME, "home_page_body_ctn")
                )
            )
            return True
        except TimeoutException:
            return False