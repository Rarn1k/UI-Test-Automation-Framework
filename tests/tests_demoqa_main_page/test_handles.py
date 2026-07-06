import logging

from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.browser_windows_page import BrowserWindowsPage
from page_objects.left_menu_page import LeftMenuPage
from page_objects.main_page import MainPage

logger = logging.getLogger(__name__)


def test_handles(driver: WebDriver, main_page: MainPage) -> None:
    logger.info("Проверяем, что главная страница не отобразилась")
    assert main_page.is_displayed(), "Главная страница не отобразилась"

    logger.info("Нажимаем на ссылку alerts, frame & Windows")
    main_page.click_alerts_windows()
    logger.info("Создаём экземпляр страницы левого меню")
    left_menu = LeftMenuPage()
    logger.info("Проверяем, что открылось левое меню")
    assert left_menu.is_displayed(), "Левое меню не отобразилось"
    logger.info("Нажимаем на ссылку Browser Windows")
    left_menu.click_browser_windows()
    logger.info("Создаём экземпляр страницы Browser Windows")
    browser = BrowserWindowsPage()
    logger.info("Проверяем, что открылась страница Browser Windows")
    assert browser.is_displayed(), "Страница Browser Windows не отобразилась"