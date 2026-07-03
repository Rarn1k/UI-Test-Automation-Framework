import logging

from selenium.webdriver.common.by import By

from element_objects.href import Href
from page_objects.base_page import BasePage
from page_objects.frames.bottom_frame_page import BottomFramePage
from page_objects.frames.upper_frame_page import UpperFramePage


logger = logging.getLogger(__name__)

class FramesPage(BasePage):
    __upper_frame = UpperFramePage()
    __bottom_frame = BottomFramePage()

    def __init__(self) -> None:
        super().__init__((By.XPATH, "//*[@class='text-center' and text()='Frames']"),
                         "Frames page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Href(self._locator, self._name).find_element().is_displayed()

    def switch_to_upper_frame(self) -> None:
        logger.info(f"Переключаемся на фрейм: {self.__upper_frame._name}")
        self.__upper_frame.switch_to_this_frame()

    def switch_to_bottom_frame(self) -> None:
        logger.info(f"Переключаемся на фрейм: {self.__bottom_frame._name}")
        self.__bottom_frame.switch_to_this_frame()
