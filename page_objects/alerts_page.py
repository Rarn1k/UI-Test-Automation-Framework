from selenium.webdriver.common.by import By

from element_objects.href import Href
from page_objects.base_page import BasePage

import logging
logger = logging.getLogger(__name__)

class AlertsPage(BasePage):
    def __init__(self) -> None:
        super().__init__((By.ID, "javascriptAlertsWrapper"), "Alerts Page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Href(self._locator, self._name).find_element().is_displayed()