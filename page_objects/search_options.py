from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page import BasePage


class SearchOptions(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self._root = self._bot.element(self._main_by)

    @property
    def _main_by(self) -> tuple:
        return By.ID, "additional_search_options"

    def get_option_element(self, option_name: str) -> WebElement:
        return self._bot.element((By.XPATH, f"//*[@data-collapse-name='{option_name}']"), self._root)

    @staticmethod
    def expand_option(element: WebElement):
        if "collapsed" in element.get_attribute("class"):
            element.click()

    def choose_option_element(self, option_element: str):
        self._bot.click((By.XPATH, f"//*[@data-loc='{option_element}']"), self._root)

    def is_option_selected(self, option_element: str) -> bool:
        element = self._bot.element((By.XPATH, f"//*[@data-loc='{option_element}']"), self._root)
        return 'checked' in element.get_attribute("class")