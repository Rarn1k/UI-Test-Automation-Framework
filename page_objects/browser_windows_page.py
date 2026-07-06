import logging

from selenium.webdriver.common.by import By

from element_objects.button import Button
from element_objects.label import Label
from page_objects.base_page import BasePage

logger = logging.getLogger(__name__)


class BrowserWindowsPage(BasePage):
    def __init__(self):
        super().__init__((By.ID, "browserWindows"), "Browser windows page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()
