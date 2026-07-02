import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from element_objects.Iframe import Iframe
from element_objects.href import Href
from page_objects.base_page import BasePage
from page_objects.nested_frames.child_iframe import ChildIFramePage
from web_driver.driver import Driver

logger = logging.getLogger(__name__)


class ParentFramePage(BasePage):
    __child_Iframe = ChildIFramePage()
    __page_text = Href((By.TAG_NAME, "body"), "Parent Frame text")
    __get_this_frame = Iframe((By.ID, "frame1"), "Parent Frame")

    def __init__(self):
        super().__init__((By.XPATH, "//*[contains(text(), 'Parent frame')]"), "Parent Frame")

    def is_displayed(self):
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Href(self._locator, self._name).find_element().is_displayed()

    def get_frame(self) -> WebElement:
        return self.__get_this_frame.find_element()

    def get_page_text(self) -> str:
        logger.info(f"Получаем текст страницы {self._name}")
        text = self.__page_text.find_element().text.strip()
        return text

    def switch_to_child_frame(self) -> None:
        logger.info(f"Переключаемся на фрейм: {self.__child_Iframe._name}")
        Driver().get_driver().switch_to.frame(self.__child_Iframe.get_frame())
