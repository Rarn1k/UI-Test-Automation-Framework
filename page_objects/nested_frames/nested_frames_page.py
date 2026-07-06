import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from element_objects.Iframe import Iframe
from element_objects.label import Label
from page_objects.base_page import BasePage

logger = logging.getLogger(__name__)

class NestedFramesPage(BasePage):
    __parent_frame = Iframe((By.ID, "frame1"), "Parent frame")

    def __init__(self) -> None:
        super().__init__((By.XPATH, "//*[@class='text-center' and text()='Nested Frames']"),
                         "Nested frames page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def get_parent_frame(self) -> WebElement:
        logger.info(f"Получаем родительский фрейм")
        return self.__parent_frame.find_element()
