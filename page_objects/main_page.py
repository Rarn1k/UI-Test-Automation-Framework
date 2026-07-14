from selenium.webdriver.common.by import By

from element_objects.button import Button
from element_objects.label import Label
from page_objects.base_page import BasePage
from utils.config.config_manager import ConfigManager
from utils.logger_manager import LoggerManager


class MainPage(BasePage):
    __alerts_href = Button((By.XPATH, "//a[@href='/alertsWindows']"), "alerts link")
    __elements_href = Button((By.XPATH, "//a[@href='/elements']"), "elements link")

    def __init__(self) -> None:
        element = Label((By.CLASS_NAME, "home-banner"), "home banner")
        super().__init__(element, "Main Page")
        self.url = ConfigManager().instance().demoqa_url

    def click_alerts_windows(self) -> None:
        LoggerManager().info("Нажимаем на ссылку alerts")
        self.__alerts_href.click()

    def click_elements(self) -> None:
        LoggerManager().info("Нажимаем на ссылку elements")
        self.__elements_href.click()
