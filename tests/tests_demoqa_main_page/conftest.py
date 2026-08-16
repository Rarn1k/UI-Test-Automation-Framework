import pytest

from page_objects.main_page import MainPage
from utils.logger_manager import LoggerManager
from web_driver.driver import Driver


@pytest.fixture
def main_page() -> MainPage:
    LoggerManager().info("Создаём экземпляр MainPage")
    main_page = MainPage()
    LoggerManager().info(f"Загружаем страницу MainPage")
    Driver().load_page(main_page.url)
    return main_page
