from dataclasses import fields

from page_objects.nav_bar import NavBar
from page_objects.search_by_sells import SearchBySells
from page_objects.search_options import SearchOptions
from page_objects.top_sellers import TopSellersPage
from tests.tests_steam_home_page.conftest import home_page
from utils.data.data_manager import DataProvider
from utils.data.data_model import DataModel


def test_case_two(driver, home_page):
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



