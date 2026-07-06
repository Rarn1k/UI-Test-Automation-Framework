import logging

from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.browser_windows_page import BrowserWindowsPage
from page_objects.left_menu_page import LeftMenuPage
from page_objects.links_page import LinksPage
from page_objects.main_page import MainPage
from page_objects.sample_page import SamplePage
from utils.tub_manager import TubManager

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

    logger.info("Создаём экземпляр Tub Manager")
    tub_manager = TubManager()
    logger.info("Сохраняем текущие вкладки")
    old_handles = tub_manager.get_all_handles()
    logger.info("Сохраняем текущую вкладку")
    browser_handle = tub_manager.get_current_handle()
    logger.info("Нажимаем на кнопку New Tab")
    browser.click_new_tab()
    logger.info("Проверяем, что открыта новая вкладка /sample со страницей sample page")
    logger.info("Переключаемся на новую вкладку")
    tub_manager.switch_to_new_window(old_handles)
    logger.info("Проверяем, что путь текущей вкладки - /sample")
    assert tub_manager.get_current_path() == "/sample", \
        f"Путь текущей вкладки: {tub_manager.get_current_path()}, ожидался /sample"
    logger.info("Создаём экземпляр страницы Sample page")
    sample = SamplePage()
    assert sample.is_displayed(), "Страница Sample page не отобразилась"

    logger.info("Закрываем текущую вкладку")
    tub_manager.close_current_window()
    logger.info("Переключаемся на вкладку страницы Browser Windows")
    tub_manager.switch_to_window(browser_handle)
    logger.info("Проверяем, что открыта страница с формой Browser Windows")
    assert browser.is_displayed(), "Страница Browser Windows не отобразилась"

    logger.info("В левом меню нажимаем на Elements")
    left_menu.click_elements_button()
    logger.info("В левом меню нажимаем Links")
    left_menu.click_links()
    logger.info("Создаём экземпляр страницы Links")
    links_page = LinksPage()
    logger.info("Проверяем, что открыта страница Links")
    assert links_page.is_displayed(), "Страница Links не отобразилась"