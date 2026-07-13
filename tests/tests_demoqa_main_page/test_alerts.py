from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.alerts_page import AlertsPage
from page_objects.left_menu_page import LeftMenuPage
from page_objects.main_page import MainPage

from utils.alert_manager import AlertManager
from utils.data.data_manager import DataManager
from utils.generate_random_string import RandomUtils
from utils.logger_manager import LoggerManager


def test_alerts(driver: WebDriver, main_page: MainPage) -> None:
    LoggerManager().get_logger().info("Проверяем, что главная страница не отобразилась")
    assert main_page.is_displayed(), "Главная страница не отобразилась"

    LoggerManager().get_logger().info("Нажимаем на ссылку alerts, frame & Windows")
    main_page.click_alerts_windows()
    LoggerManager().get_logger().info("Создаём экземпляр страницы левого меню")
    left_menu = LeftMenuPage()
    LoggerManager().get_logger().info("Проверяем, что открылось левое меню")
    assert left_menu.is_displayed(), "Левое меню не отобразилось"
    LoggerManager().get_logger().info("Нажимаем на ссылку alerts")
    left_menu.click_alerts()
    LoggerManager().get_logger().info("Создаём экземпляр страницы alerts")
    alerts = AlertsPage()
    LoggerManager().get_logger().info("Проверяем, что открылась страница alerts")
    assert alerts.is_displayed(), "Страница alerts не отобразилась"

    LoggerManager().get_logger().info("Нажимаем на кнопку alert")
    alerts.click_alert()
    LoggerManager().get_logger().info("Создаём экземпляр алерт менеджера")
    expected_alert_text = DataManager().instance().alert_text
    LoggerManager().get_logger().info(f"Проверяем, что открылся алерт с текстом {expected_alert_text}")
    assert AlertManager.get_alert_text() == expected_alert_text, f"Текст алерта не совпал с ожидаемым {expected_alert_text}"

    LoggerManager().get_logger().info("Принимаем алерт")
    AlertManager.accept_alert()
    LoggerManager().get_logger().info("Проверяем, что алерт закрылся")
    assert AlertManager.wait_alert_closed(), "Алерт не закрылся"

    LoggerManager().get_logger().info("Нажимаем на кнопку confirm box")
    alerts.click_confirm_alert()
    LoggerManager().get_logger().info("Создаём экземпляр confirm box")
    expected_confirm_text = DataManager().instance().confirm_text
    LoggerManager().get_logger().info(f"Проверяем, что открылся confirm алерт с текстом {expected_confirm_text}")
    assert AlertManager.get_alert_text() == expected_confirm_text, \
        f"Текст алерта не совпал с ожидаемым {expected_confirm_text}"

    LoggerManager().get_logger().info("Принимаем confirm алерт")
    AlertManager.accept_alert()
    LoggerManager().get_logger().info("Проверяем, что confirm алерт закрылся")
    assert AlertManager.wait_alert_closed(), "Confirm алерт не закрылся"
    expected_confirm_result_text = DataManager().instance().confirm_result_text
    LoggerManager().get_logger().info(f"Проверяем, что появилась надпись {expected_confirm_result_text}")
    assert alerts.find_confirm_text() == expected_confirm_result_text, \
        f"Не появилась надпись {expected_confirm_result_text}"

    LoggerManager().get_logger().info("Нажимаем на кнопку prompt alert")
    alerts.click_prompt_alert()
    LoggerManager().get_logger().info("Создаём экземпляр prompt алерта")
    expected_prompt_text = DataManager().instance().prompt_text
    LoggerManager().get_logger().info(f"Проверяем, что открылся prompt алерт с текстом {expected_prompt_text}")
    assert AlertManager.get_alert_text() == expected_prompt_text, \
        f"Текст алерта не совпал с ожидаемым {expected_prompt_text}"

    random_string = RandomUtils.generate_random_string()
    LoggerManager().get_logger().info(f"Вводим текст {random_string}")
    AlertManager.send_keys(random_string)
    LoggerManager().get_logger().info("Нажимаем ОК в prompt alert")
    AlertManager.accept_alert()
    LoggerManager().get_logger().info("Проверяем, что prompt алерт закрылся")
    assert AlertManager.wait_alert_closed(), "Prompt алерт не закрылся"
    expected_prompt_result_text = DataManager().instance().prompt_result_text + random_string
    LoggerManager().get_logger().info(f"Проверяем, что появилась надпись {expected_prompt_result_text}")
    assert alerts.find_prompt_text() == expected_prompt_result_text, \
        f"Не появилась надпись {expected_prompt_result_text}"
