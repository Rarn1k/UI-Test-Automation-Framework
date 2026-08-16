from selenium.webdriver.common.by import By

from element_objects.label import Label
from page_objects.base_page import BasePage
from utils.logger_manager import LoggerManager


class BottomFramePage(BasePage):
    __page_text = Label((By.ID, "sampleHeading"), "Bottom frame text")

    def __init__(self):
        element = Label((By.XPATH, "//*[contains(text(), 'This is a sample page')]"), "Sample page")
        super().__init__(element, "Bottom frame page")

    def get_page_text(self) -> str:
        LoggerManager().info(f"Получаем текст страницы {self._name}")
        return self.__page_text.find_element().text.strip()
