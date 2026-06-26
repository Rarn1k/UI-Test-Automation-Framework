from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SearchBySells(BasePage):
    @property
    def _main_by(self) -> tuple[str, str]:
        return By.ID, "advsearchform"
