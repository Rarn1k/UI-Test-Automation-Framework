from selenium.webdriver.common.by import By

from element_objects.button import Button
from element_objects.label import Label
from page_objects.base_page import BasePage

import logging
logger = logging.getLogger(__name__)

class AlertsPage(BasePage):
    __alert_button = Button((By.ID, "alertButton"), "Alert Button")
    __confirm_button = Button((By.ID, "confirmButton"), "Confirm Button")
    __confirm_text = Label((By.ID, "confirmResult"), "Confirm text")
    __prompt_button = Button((By.ID, "promtButton"), "Prompt Button")
    __prompt_text = Label((By.ID, "promptResult"), "Prompt text")

    def __init__(self) -> None:
        super().__init__((By.ID, "javascriptAlertsWrapper"), "Alerts Page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def click_alert(self) -> None:
        logger.info(f"Нажимаем на кнопку алерта")
        self.__alert_button.click()

    def click_confirm_alert(self) -> None:
        logger.info(f"Нажимаем на кнопку confirm алерта")
        self.__confirm_button.click()

    def find_confirm_text(self) -> str:
        logger.info(f"Получаем текст рядом с кнопкой confirm алерта")
        return self.__confirm_text.find_element().text

    def click_prompt_alert(self) -> None:
        logger.info(f"Нажимаем на кнопку prompt алерта")
        self.__prompt_button.click()

    def find_prompt_text(self) -> str:
        logger.info(f"Получаем текст рядом с кнопкой prompt алерта")
        return self.__prompt_text.find_element().text