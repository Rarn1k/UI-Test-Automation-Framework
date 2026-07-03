import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from element_objects.Iframe import Iframe
from element_objects.href import Href
from page_objects.frames.base_frame_page import BaseFramePage
from page_objects.frames.nested_frames.child_iframe import ChildIFramePage

logger = logging.getLogger(__name__)


class ParentFramePage(BaseFramePage):
    __this_frame = Iframe((By.ID, "frame1"), "Parent frame")

    __child_Iframe = ChildIFramePage()
    __page_text = Href((By.TAG_NAME, "body"), "Parent frame text")

    def __init__(self):
        super().__init__((By.XPATH, "//*[contains(text(), 'Parent frame')]"), "Parent frame page")

    def is_displayed(self):
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Href(self._locator, self._name).find_element().is_displayed()

    def _get_this_frame(self) -> WebElement:
        return self.__this_frame.find_element()

    def get_page_text(self) -> str:
        logger.info(f"Получаем текст страницы {self._name}")
        return self.__page_text.find_element().text.strip()

    def switch_to_child_frame(self) -> None:
        logger.info(f"Переключаемся на фрейм: {self.__child_Iframe._name}")
        self.__child_Iframe.switch_to_this_frame()
