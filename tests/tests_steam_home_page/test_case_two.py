from tests.tests_steam_home_page.conftest import home_page



def test_case_one(driver, home_page):
    home_page.load_page()
    assert home_page.is_loaded()
    home_page.click_top_sellers()
    assert home_page.is_top_sellers_active()