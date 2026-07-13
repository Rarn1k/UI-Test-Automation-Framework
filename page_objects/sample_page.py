import logging

from selenium.webdriver.common.by import By

from element_objects.label import Label
from page_objects.base_page import BasePage
from utils.logger_manager import LoggerManager

logger = logging.getLogger(__name__)


class SamplePage(BasePage):
    def __init__(self) -> None:
        super().__init__((By.ID, "sampleHeading"), "Sample page")

    def is_displayed(self) -> bool:
        LoggerManager().get_logger().info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()
