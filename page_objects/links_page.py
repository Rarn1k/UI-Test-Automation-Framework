import logging

from selenium.webdriver.common.by import By

from element_objects.href import Href
from element_objects.label import Label
from page_objects.base_page import BasePage

logger = logging.getLogger(__name__)


class LinksPage(BasePage):
    __home_href = Href((By.LINK_TEXT, 'Home'), "home link")

    def __init__(self) -> None:
        super().__init__((By.ID, "linkWrapper"), "Links page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def click_home_link(self) -> None:
        logger.info("Нажимаем на ссылку открытия домашней страницы")
        self.__home_href.click()