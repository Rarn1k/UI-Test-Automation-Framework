from selenium.webdriver.common.by import By

from element_objects.button import Button
from element_objects.href import Href
from element_objects.label import Label
from page_objects.base_page import BasePage

import logging

logger = logging.getLogger(__name__)

class LeftMenuPage(BasePage):
    __alerts_href = Href((By.XPATH, "//a[@href='/alerts']"), "alerts link")
    __nested_frames_href = Href((By.XPATH, "//a[@href='/nestedframes']"), "nested frames link")
    __frames_href = Href((By.XPATH, "//a[@href='/frames']"), "frames link")
    __web_tables_href = Href((By.XPATH, "//a[@href='/webtables']"), "web tables link")
    __browser_href = Href((By.XPATH, "//a[@href='/browser-windows']"), "browser windows link")
    __elements_button = Button((By.XPATH, "//*[text()='Elements']"), "elements button")
    __links_href = Href((By.XPATH, "//a[@href='/links']"), "links link")

    def __init__(self) -> None:
        super().__init__((By.CLASS_NAME, "left-pannel"), "Left Menu Page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def click_alerts(self) -> None:
        self.__alerts_href.click()

    def click_nested_frames(self) -> None:
        self.__nested_frames_href.click()

    def click_frames(self) -> None:
        self.__frames_href.click()

    def click_web_tables(self) -> None:
        self.__web_tables_href.click()

    def click_browser_windows(self) -> None:
        self.__browser_href.click()

    def click_elements_button(self) -> None:
        self.__elements_button.click()

    def click_links(self) -> None:
        self.__links_href.click()