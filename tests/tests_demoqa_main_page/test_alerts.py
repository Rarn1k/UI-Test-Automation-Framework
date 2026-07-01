from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.main_page import MainPage


def test_alerts(driver: WebDriver, main_page: MainPage) -> None:
    assert main_page.is_displayed(), "Главная страница не отобразилась"