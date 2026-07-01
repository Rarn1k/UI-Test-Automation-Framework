from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.main_page import MainPage

import logging
logger = logging.getLogger(__name__)


def test_alerts(driver: WebDriver, main_page: MainPage) -> None:
    logger.info("Assert, что главная страница не отобразилась")
    assert main_page.is_displayed(), "Главная страница не отобразилась"