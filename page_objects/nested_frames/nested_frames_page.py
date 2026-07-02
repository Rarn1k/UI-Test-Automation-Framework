import logging

from selenium.webdriver.common.by import By

from element_objects.href import Href
from page_objects.base_page import BasePage
from page_objects.nested_frames.parent_frame_page import ParentFramePage
from web_driver.driver import Driver

logger = logging.getLogger(__name__)

class NestedFrames(BasePage):
    __parent_frame = ParentFramePage()

    def __init__(self) -> None:
        super().__init__((By.XPATH, "//*[@class='text-center' and text()='Nested Frames']"),
                         "Nested Frames Page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Href(self._locator, self._name).find_element().is_displayed()

    def get_parent_frame_text(self) -> bool:
        logger.info(f"Получаем текст страницы {self.__parent_frame._name}")
        return self.__parent_frame.is_displayed()

    def switch_to_parent_frame(self) -> None:
        logger.info(f"Переключаемся на фрейм: {self.__parent_frame._name}")
        Driver().get_driver().switch_to.frame(self.__parent_frame.get_frame())