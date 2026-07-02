import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from element_objects.Iframe import Iframe
from element_objects.href import Href
from page_objects.base_page import BasePage

logger = logging.getLogger(__name__)


class ChildIFramePage(BasePage):
    __page_text = Href((By.TAG_NAME, "body"), "Child Frame text")
    __get_this_frame = Iframe((By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]"), "Child Iframe")

    def __init__(self):
        super().__init__((By.XPATH, "//*[contains(text(), 'Child Iframe')]"), "Child Frame")

    def is_displayed(self):
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Href(self._locator, self._name).find_element().is_displayed()

    def get_frame(self) -> WebElement:
        return self.__get_this_frame.find_element()

    def get_page_text(self) -> str:
        logger.info(f"Получаем текст страницы {self._name}")
        text = self.__page_text.find_element().text.strip()
        return text