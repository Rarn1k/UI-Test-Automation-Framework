from selenium import webdriver

from page_objects.game_page import GamePage
from page_objects.home_page import HomePage
from page_objects.nav_bar import NavBar
from page_objects.search_by_sells import SearchBySells
from page_objects.search_options import SearchOptions
from page_objects.top_sellers import TopSellersPage
from tests.tests_steam_home_page.conftest import home_page
from utils.data.data_manager import DataProvider


def test_case_two(driver: webdriver, home_page: HomePage) -> None:
    home_page.load_page()
    assert home_page.is_loaded()

    nav_bar = NavBar(driver)
    assert nav_bar.is_loaded()

    nav_bar.click_browse()
    nav_bar.click_top_sellers()
    top_sellers = TopSellersPage(driver)
    assert top_sellers.is_loaded()

    top_sellers.click_more_top_sellers()
    search_by_sells = SearchBySells(driver)
    assert search_by_sells.is_loaded()

    search_options = SearchOptions(driver)
    assert search_options.is_loaded()

    filters = DataProvider().instance().filters
    for name in filters.keys():
        search_element = search_options.get_option_element(name)
        search_options.expand_option(search_element)
        for value in filters[name]:
            search_options.choose_option_element(value)
            assert search_options.is_option_selected(value)
    results_count = search_options.get_results_count()
    search_options.wait_change_results(results_count)
    rows = search_options.get_rows()
    assert search_options.get_results_count() == len(rows)

    first_game = rows[0]
    first_game_dict = {'title': search_options.get_game_title(first_game),
                       'release_date': search_options.get_game_release_date(first_game),
                       'price': search_options.get_game_price(first_game)}

    search_options.click_on_element(first_game)
    game_page = GamePage(driver)
    assert game_page.is_loaded()
    assert first_game_dict['title'] == game_page.get_title()
    assert first_game_dict['release_date'] == game_page.get_release()
    assert first_game_dict['price'] == game_page.get_price()
