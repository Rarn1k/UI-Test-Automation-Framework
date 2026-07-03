import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from element_objects.Iframe import Iframe
from element_objects.href import Href
from page_objects.frames.base_frame_page import BaseFramePage

logger = logging.getLogger(__name__)


class UpperFramePage(BaseFramePage):
    __this_frame = Iframe((By.ID, "frame1"), "Upper frame")

    __page_text = Href((By.ID, "sampleHeading"), "Upper frame text")

    def __init__(self):
        super().__init__((By.XPATH, "//*[contains(text(), 'This is a sample page')]"), "Upper frame page")

    def is_displayed(self) -> bool:
        return Href(self._locator, self._name).find_element().is_displayed()

    def _get_this_frame(self) -> WebElement:
        return self.__this_frame.find_element()

    def get_page_text(self) -> str:
        logger.info(f"Получаем текст страницы {self._name}")
        return self.__page_text.find_element().text.strip()

