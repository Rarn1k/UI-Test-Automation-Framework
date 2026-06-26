from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from page_objects.base_page import BasePage
from utils.text_handler import TextHandler


class SearchOptions(BasePage):
    _results_count_by = (By.XPATH,
                         "//*[contains(@class, 'search_results_count') or @class='search_results_filtered_warning']")
    _rows_by = By.XPATH, "//*[contains(@class,'search_result_row')]"
    _game_title_by = By.XPATH, ".//*[contains(@class, 'title')]"
    _game_released_by = By.XPATH, ".//*[contains(@class, 'search_released')]"
    _game_price_by = By.XPATH, ".//*[contains(@class, 'discount_final_price')]"

    def __init__(self, driver: webdriver) -> None:
        super().__init__(driver)
        self._root = self._bot.element(self._main_by)

    @property
    def _main_by(self) -> tuple[str, str]:
        return By.ID, "additional_search_options"

    def get_option_element(self, option_name: str) -> WebElement:
        return self._bot.element((By.XPATH, f"//*[@data-collapse-name='{option_name}']"), self._root)

    @staticmethod
    def expand_option(element: WebElement) -> None:
        if "collapsed" in element.get_attribute("class"):
            element.click()

    def choose_option_element(self, option_element: str) -> None:
        self._bot.click((By.XPATH, f"//*[@data-loc='{option_element}']"), self._root)

    def is_option_selected(self, option_element: str) -> bool:
        element = self._bot.element((By.XPATH, f"//*[@data-loc='{option_element}']"), self._root)
        return 'checked' in element.get_attribute("class")

    def get_results_count(self) -> int:
        text = self._bot.element(self._results_count_by).get_attribute("textContent")
        return TextHandler.get_num_from_text(text)

    def get_rows(self) -> list[WebElement]:
        return self._bot.elements(self._rows_by)

    def wait_change_results(self, old_num: int) -> None:
        new_num = self.get_results_count()
        try:
            self._bot.wait_until(lambda _: new_num != old_num)
        except TimeoutException:
            pass

    def get_value_by_class_attr_from_el(self, element: WebElement, attr: str) -> str:
        locator = By.CLASS_NAME, f"{attr}"
        return self._bot.element(locator, element).text.strip()

    def get_game_title(self, game: WebElement) -> str:
        return self._bot.element(self._game_title_by, game).text.strip()

    def get_game_release_date(self, game: WebElement) -> str:
        return self._bot.element(self._game_released_by, game).text.strip()

    def get_game_price(self, game: WebElement) -> int:
        text = self._bot.element(self._game_price_by, game).text
        return TextHandler.get_num_from_text(text)

    @staticmethod
    def click_on_element(element: WebElement) -> None:
        element.click()
