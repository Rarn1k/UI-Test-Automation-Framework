from selenium.webdriver.common.by import By

from element_objects.button import Button
from page_objects.base_page import BasePage
from utils.logger_manager import LoggerManager


class WebTablesPage(BasePage):
    __add_button = Button((By.ID, "addNewRecordButton"), "Add record button")

    def __init__(self) -> None:
        super().__init__((By.CLASS_NAME, "web-tables-wrapper"), "Web tables page")

    def click_add_new_record(self) -> None:
        LoggerManager().info(f"Добавляем новую запись")
        self.__add_button.click()
