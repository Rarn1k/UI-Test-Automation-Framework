from selenium.webdriver.common.by import By

from element_objects.label import Label
from page_objects.base_page import BasePage
from utils.logger_manager import LoggerManager


class ParentFramePage(BasePage):
    __page_text = Label((By.XPATH, "//*[contains(text(), 'Parent frame')]"), "Parent frame text")

    def __init__(self) -> None:
        super().__init__((By.XPATH, "//*[contains(text(), 'Parent frame')]"), "Parent frame page")

    def is_displayed(self) -> bool:
        return Label(self._locator, self._name).find_element().is_displayed()

    def get_page_text(self) -> str:
        LoggerManager().get_logger().info(f"Получаем текст страницы {self._name}")
        return self.__page_text.find_element().text.strip()
