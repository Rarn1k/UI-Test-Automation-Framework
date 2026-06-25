from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.base_page import BasePage
from utils.config.config_manager import ConfigProvider
from utils.text_handler import TextHandler


class SearchOptions(BasePage):
    _results_count_by = (By.XPATH,
                         "//*[contains(@class, 'search_results_count') or @class='search_results_filtered_warning']")
    _rows_by = By.XPATH, "//*[contains(@class,'search_result_row')]"
    _game_name_by = By.XPATH, ".//*[contains(@class, 'title')]"

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

    def get_results_count(self) -> int:
        text = self._bot.element(self._results_count_by).get_attribute("textContent")
        return TextHandler.get_num_from_text(text)

    def get_rows(self) -> list[WebElement]:
        return self._bot.elements(self._rows_by)

    def wait_change_results(self, old_num: int):
        new_num = self.get_results_count()
        try:
            self._bot.wait_until(lambda _: new_num != old_num)
        except TimeoutException:
            pass
