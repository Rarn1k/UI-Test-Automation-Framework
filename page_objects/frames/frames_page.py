import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from element_objects.Iframe import Iframe
from element_objects.label import Label
from page_objects.base_page import BasePage



logger = logging.getLogger(__name__)

class FramesPage(BasePage):
    __upper_frame = Iframe((By.ID, "frame1"), "Upper frame")
    __bottom_frame = Iframe((By.ID, "frame2"), "Bottom frame")

    def __init__(self) -> None:
        super().__init__((By.XPATH, "//*[@class='text-center' and text()='Frames']"), "Frames page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def get_upper_frame(self) -> WebElement:
        logger.info("Получаем верхний фрейм")
        return self.__upper_frame.find_element()

    def get_bottom_frame(self) -> WebElement:
        logger.info("Получаем нижний фрейм")
        return self.__bottom_frame.find_element()
