from selenium.webdriver.common.by import By

from element_objects.button import Button
from element_objects.label import Label
from page_objects.base_page import BasePage
from utils.logger_manager import LoggerManager


class LinksPage(BasePage):
    __home_href = Button((By.LINK_TEXT, 'Home'), "home link")

    def __init__(self) -> None:
        super().__init__((By.ID, "linkWrapper"), "Links page")

    def is_displayed(self) -> bool:
        LoggerManager().info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def click_home_link(self) -> None:
        LoggerManager().info("Нажимаем на ссылку открытия домашней страницы")
        self.__home_href.click()
