import pytest

from page_objects.main_page import MainPage

import logging

from web_driver.driver import Driver

logger = logging.getLogger(__name__)

@pytest.fixture
def main_page() -> MainPage:
    logger.info("Создаём экземпляр MainPage")
    main_page = MainPage()
    logger.info(f"Загружаем страницу MainPage")
    Driver().load_page(main_page.url)
    return main_page