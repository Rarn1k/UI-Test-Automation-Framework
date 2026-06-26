from selenium import webdriver

from page_objects.about_page import AboutPage
from page_objects.home_page import HomePage
from page_objects.supernav_bar import SupernavBar
from tests.tests_steam_home_page.conftest import home_page


def test_case_one(driver: webdriver, home_page: HomePage) -> None:
    home_page.load_page()
    assert home_page.is_loaded()
    supernav_bar = SupernavBar(driver)
    assert supernav_bar.is_loaded()
    supernav_bar.click_about()
    about_page = AboutPage(driver)
    assert about_page.is_loaded()
    assert about_page.get_gamers_in_game() < about_page.get_gamers_online()
    supernav_bar = SupernavBar(driver)
    supernav_bar.click_store()
    store_page = HomePage(driver)
    assert store_page.is_loaded()