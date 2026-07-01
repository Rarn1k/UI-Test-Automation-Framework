import pytest

from page_objects.main_page import MainPage

import logging
logger = logging.getLogger(__name__)

@pytest.fixture
def main_page() -> MainPage:
    logger.info("Создаём экземпляр MainPage")
    main_page = MainPage()
    logger.info(f"Загружаем страницу {main_page._name}")
    main_page.load_page()
    return main_page