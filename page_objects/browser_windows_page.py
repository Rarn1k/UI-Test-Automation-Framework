import logging

from selenium.webdriver.common.by import By

from element_objects.button import Button
from element_objects.label import Label
from page_objects.base_page import BasePage

logger = logging.getLogger(__name__)


class BrowserWindowsPage(BasePage):
    __new_tab_button = Button((By.ID, "tabButton"), "New tab button")

    def __init__(self) -> None:
        super().__init__((By.ID, "browserWindows"), "Browser windows page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def click_new_tab(self) -> None:
        logger.info(f"Нажимаем на кнопку открытия новой вкладки")
        self.__new_tab_button.click()
