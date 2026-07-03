import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from element_objects.Iframe import Iframe
from element_objects.label import Label
from page_objects.base_page import BasePage

logger = logging.getLogger(__name__)


class ParentFramePage(BasePage):
    __child_Iframe = Iframe((By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]"), "Child Iframe")
    __page_text = Label((By.TAG_NAME, "body"), "Parent frame text")

    def __init__(self):
        super().__init__((By.XPATH, "//*[contains(text(), 'Parent frame')]"), "Parent frame page")

    def is_displayed(self):
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def get_page_text(self) -> str:
        logger.info(f"Получаем текст страницы {self._name}")
        return self.__page_text.find_element().text.strip()

    def get_child_frame(self) -> WebElement:
        return self.__child_Iframe.find_element()
