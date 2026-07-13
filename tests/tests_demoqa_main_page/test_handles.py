from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.browser_windows_page import BrowserWindowsPage
from page_objects.left_menu_page import LeftMenuPage
from page_objects.links_page import LinksPage
from page_objects.main_page import MainPage
from page_objects.sample_page import SamplePage
from utils.logger_manager import LoggerManager
from utils.tub_manager import TubManager


def test_handles(driver: WebDriver, main_page: MainPage) -> None:
    LoggerManager().get_logger().info("Проверяем, что главная страница не отобразилась")
    assert main_page.is_displayed(), "Главная страница не отобразилась"

    LoggerManager().get_logger().info("Нажимаем на ссылку alerts, frame & Windows")
    main_page.click_alerts_windows()
    LoggerManager().get_logger().info("Создаём экземпляр страницы левого меню")
    left_menu = LeftMenuPage()
    LoggerManager().get_logger().info("Проверяем, что открылось левое меню")
    assert left_menu.is_displayed(), "Левое меню не отобразилось"
    LoggerManager().get_logger().info("Нажимаем на ссылку Browser Windows")
    left_menu.click_browser_windows()
    LoggerManager().get_logger().info("Создаём экземпляр страницы Browser Windows")
    browser = BrowserWindowsPage()
    LoggerManager().get_logger().info("Проверяем, что открылась страница Browser Windows")
    assert browser.is_displayed(), "Страница Browser Windows не отобразилась"

    LoggerManager().get_logger().info("Создаём экземпляр Tub Manager")
    tub_manager = TubManager()
    LoggerManager().get_logger().info("Сохраняем текущие вкладки")
    old_handles = tub_manager.get_all_handles()
    LoggerManager().get_logger().info("Сохраняем текущую вкладку")
    browser_handle = tub_manager.get_current_handle()
    LoggerManager().get_logger().info("Нажимаем на кнопку New Tab")
    browser.click_new_tab()
    LoggerManager().get_logger().info("Проверяем, что открыта новая вкладка /sample со страницей sample page")
    LoggerManager().get_logger().info("Переключаемся на новую вкладку")
    tub_manager.switch_to_new_window(old_handles)
    LoggerManager().get_logger().info("Проверяем, что путь текущей вкладки - /sample")
    assert tub_manager.get_current_path() == "/sample", \
        f"Путь текущей вкладки: {tub_manager.get_current_path()}, ожидался /sample"
    LoggerManager().get_logger().info("Создаём экземпляр страницы Sample page")
    sample = SamplePage()
    LoggerManager().get_logger().info("Проверяем, что открыта страница Sample page")
    assert sample.is_displayed(), "Страница Sample page не отобразилась"

    LoggerManager().get_logger().info("Закрываем текущую вкладку")
    tub_manager.close_current_window()
    LoggerManager().get_logger().info("Переключаемся на вкладку страницы Browser Windows")
    tub_manager.switch_to_window(browser_handle)
    LoggerManager().get_logger().info("Проверяем, что открыта страница с формой Browser Windows")
    assert browser.is_displayed(), "Страница Browser Windows не отобразилась"

    LoggerManager().get_logger().info("В левом меню нажимаем на Elements")
    left_menu.click_elements_button()
    LoggerManager().get_logger().info("В левом меню нажимаем Links")
    left_menu.click_links()
    LoggerManager().get_logger().info("Создаём экземпляр страницы Links page")
    links_page = LinksPage()
    LoggerManager().get_logger().info("Проверяем, что открыта страница Links page")
    assert links_page.is_displayed(), "Страница Links page не отобразилась"

    LoggerManager().get_logger().info("Сохраняем текущие вкладки")
    old_handles = tub_manager.get_all_handles()
    LoggerManager().get_logger().info("Нажимаем на ссылку Home")
    links_page.click_home_link()
    LoggerManager().get_logger().info("Переключаемся на новую вкладку")
    tub_manager.switch_to_new_window(old_handles)
    LoggerManager().get_logger().info("Проверяем, что открыта страница main page")
    assert main_page.is_displayed(), "Страница main page не отобразилась"

    LoggerManager().get_logger().info("Переключаемся на прошлую вкладку")
    tub_manager.switch_to_previous_window()
    LoggerManager().get_logger().info("Проверяем, что открыта страница Links page")
    assert links_page.is_displayed(), "Страница Links page не отобразилась"
