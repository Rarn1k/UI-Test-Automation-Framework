from selenium.webdriver.common.by import By

from element_objects.button import Button
from element_objects.label import Label
from page_objects.base_page import BasePage

from utils.logger_manager import LoggerManager


class LeftMenuPage(BasePage):
    __alerts_href = Button((By.XPATH, "//a[@href='/alerts']"), "alerts link")
    __nested_frames_href = Button((By.XPATH, "//a[@href='/nestedframes']"), "nested frames link")
    __frames_href = Button((By.XPATH, "//a[@href='/frames']"), "frames link")
    __web_tables_href = Button((By.XPATH, "//a[@href='/webtables']"), "web tables link")
    __browser_href = Button((By.XPATH, "//a[@href='/browser-windows']"), "browser windows link")
    __elements_button = Button((By.XPATH, "//*[text()='Elements']"), "elements button")
    __links_href = Button((By.XPATH, "//a[@href='/links']"), "links link")

    def __init__(self) -> None:
        element = Label((By.CLASS_NAME, "left-pannel"), "left pannel element")
        super().__init__(element, "Left Menu Page")

    def click_alerts(self) -> None:
        LoggerManager().info("Нажимаем на ссылку alerts")
        self.__alerts_href.click()

    def click_nested_frames(self) -> None:
        LoggerManager().info("Нажимаем на ссылку nested frames")
        self.__nested_frames_href.click()

    def click_frames(self) -> None:
        LoggerManager().info("Нажимаем на ссылку frames")
        self.__frames_href.click()

    def click_web_tables(self) -> None:
        LoggerManager().info("Нажимаем на ссылку web tables")
        self.__web_tables_href.click()

    def click_browser_windows(self) -> None:
        LoggerManager().info("Нажимаем на ссылку browser windows")
        self.__browser_href.click()

    def click_elements_button(self) -> None:
        LoggerManager().info("Нажимаем на кнопку elements")
        self.__elements_button.click()

    def click_links(self) -> None:
        LoggerManager().info("Нажимаем на ссылку links")
        self.__links_href.click()
