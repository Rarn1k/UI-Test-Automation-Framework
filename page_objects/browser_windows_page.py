from selenium.webdriver.common.by import By

from element_objects.button import Button
from page_objects.base_page import BasePage
from utils.logger_manager import LoggerManager


class BrowserWindowsPage(BasePage):
    __new_tab_button = Button((By.ID, "tabButton"), "New tab button")

    def __init__(self) -> None:
        super().__init__((By.ID, "browserWindows"), "Browser windows page")

    def click_new_tab(self) -> None:
        LoggerManager().info(f"Нажимаем на кнопку открытия новой вкладки")
        self.__new_tab_button.click()
