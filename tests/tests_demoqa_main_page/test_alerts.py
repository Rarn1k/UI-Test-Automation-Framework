from selenium.webdriver.remote.webdriver import WebDriver

from alerts.alert import Alert
from page_objects.alerts_page import AlertsPage
from page_objects.left_menu_page import LeftMenuPage
from page_objects.main_page import MainPage

import logging

from utils.data.data_manager import DataManager

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
    assert alerts.is_displayed(), "Страница alerts не отобразилась"

    logger.info("Нажимаем на кнопку alert")
    alerts.click_alert()
    logger.info("Создаём экземпляр алерта")
    alert = Alert()
    expected_alert_text = DataManager().instance().alert_text
    logger.info(f"Проверяем, что открылся алерт с текстом {expected_alert_text}")
    assert alert.get_alert_text() == expected_alert_text, f"Текст алерта не совпал с ожидаемым {expected_alert_text}"

    logger.info("Принимаем алерт")
    alert.accept_alert()
    logger.info("Проверяем, что алерт закрылся")
    assert alert.wait_alert_closed(), "Алерт не закрылся"

    logger.info("Нажимаем на кнопку confirm box")
    alerts.click_confirm_alert()
    logger.info("Создаём экземпляр confirm box")
    confirm_alert = Alert()
    expected_confirm_text = DataManager().instance().confirm_text
    logger.info(f"Проверяем, что открылся confirm алерт с текстом {expected_confirm_text}")
    assert confirm_alert.get_alert_text() == expected_confirm_text, \
        f"Текст алерта не совпал с ожидаемым {expected_confirm_text}"

    logger.info("Принимаем confirm алерт")
    confirm_alert.accept_alert()
    logger.info("Проверяем, что confirm алерт закрылся")
    assert confirm_alert.wait_alert_closed(), "Confirm алерт не закрылся"
    expected_confirm_result_text = DataManager().instance().confirm_result_text
    logger.info(f"Проверяем, что появилась надпись {expected_confirm_result_text}")
    assert alerts.find_confirm_text() == expected_confirm_result_text,\
        f"Не появилась надпись {expected_confirm_result_text}"

    logger.info("Нажимаем на кнопку prompt alert")
    alerts.click_prompt_alert()
    logger.info("Создаём экземпляр prompt алерта")
    prompt_alert = Alert()
    expected_prompt_text = DataManager().instance().prompt_text
    logger.info(f"Проверяем, что открылся prompt алерт с текстом {expected_prompt_text}")
    assert prompt_alert.get_alert_text() == expected_prompt_text, \
        f"Текст алерта не совпал с ожидаемым {expected_prompt_text}"
