from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.alerts_page import AlertsPage
from page_objects.left_menu_page import LeftMenuPage
from page_objects.main_page import MainPage

import logging
logger = logging.getLogger(__name__)


def test_alerts(driver: WebDriver, main_page: MainPage) -> None:
    logger.info("Проверяем, что главная страница не отобразилась")
    assert main_page.is_displayed(), "Главная страница не отобразилась"

    logger.info("Нажимаем на ссылку alerts, frame & Windows")
    main_page.click_alerts_windows()
    logger.info("Создаём экземпляр страницы левого меню")
    left_menu = LeftMenuPage()
    logger.info("Проверяем, что открылось левое меню")
    assert left_menu.is_displayed(), "Левое меню не отобразилось"
    logger.info("Нажимаем на ссылку alerts")
    left_menu.click_alerts()
    logger.info("Создаём экземпляр страницы alerts")
    alerts = AlertsPage()
    logger.info("Проверяем, что открылась страница alerts")
    assert alerts.is_displayed()
