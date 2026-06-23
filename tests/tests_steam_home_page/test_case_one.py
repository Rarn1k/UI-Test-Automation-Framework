from tests.tests_steam_home_page.conftest import home_page


def test_case_one(driver, home_page):
    home_page.load_page()
    assert home_page.is_loaded()
    about_page = home_page.click_about()
    assert about_page.is_loaded()