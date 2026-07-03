import logging

from selenium.webdriver.common.by import By

from element_objects.href import Href
from page_objects.base_page import BasePage
from page_objects.frames.nested_frames.parent_frame_page import ParentFramePage

logger = logging.getLogger(__name__)

class NestedFramesPage(BasePage):
    __parent_frame = ParentFramePage()

    def __init__(self) -> None:
        super().__init__((By.XPATH, "//*[@class='text-center' and text()='Nested Frames']"),
                         "Nested frames page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Href(self._locator, self._name).find_element().is_displayed()

    def switch_to_parent_frame(self) -> None:
        logger.info(f"Переключаемся на фрейм: {self.__parent_frame._name}")
        self.__parent_frame.switch_to_this_frame()