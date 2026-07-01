import pytest

from page_objects.main_page import MainPage


@pytest.fixture
def main_page() -> MainPage:
    main_page = MainPage()
    main_page.load_page()
    return main_page