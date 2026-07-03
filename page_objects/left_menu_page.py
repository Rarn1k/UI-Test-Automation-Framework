from selenium.webdriver.common.by import By

from element_objects.href import Href
from page_objects.base_page import BasePage

import logging

logger = logging.getLogger(__name__)

class LeftMenuPage(BasePage):
    __alerts_href = Href((By.XPATH, "//a[@href='/alerts']"), "alerts link")
    __nested_frames_href = Href((By.XPATH, "//a[@href='/nestedframes']"), "nested frames link")
    __frames_href = Href((By.XPATH, "//a[@href='/frames']"), "frames link")
    __web_tables_href = Href((By.XPATH, "//a[@href='/webtables']"), "web tables link")

    def __init__(self) -> None:
        super().__init__((By.CLASS_NAME, "left-pannel"), "Left Menu Page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Href(self._locator, self._name).find_element().is_displayed()

    def click_alerts(self) -> None:
        self.__alerts_href.click()

    def click_nested_frames(self) -> None:
        self.__nested_frames_href.click()

    def click_frames(self) -> None:
        self.__frames_href.click()

    def click_web_tables(self) -> None:
        self.__web_tables_href.click()
