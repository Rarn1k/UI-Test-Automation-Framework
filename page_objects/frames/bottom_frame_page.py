import logging

from selenium.webdriver.common.by import By

from element_objects.label import Label
from page_objects.base_page import BasePage

logger = logging.getLogger(__name__)


class BottomFramePage(BasePage):
    __page_text = Label((By.ID, "sampleHeading"), "Bottom frame text")

    def __init__(self):
        super().__init__((By.XPATH, "//*[contains(text(), 'This is a sample page')]"), "Bottom frame page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def get_page_text(self) -> str:
        logger.info(f"Получаем текст страницы {self._name}")
        return self.__page_text.find_element().text.strip()
