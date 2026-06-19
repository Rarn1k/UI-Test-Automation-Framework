import pytest

from web_driver.chrome_driver import ChromeDriver


@pytest.fixture(scope="function")
def driver():
    driver = ChromeDriver().get_driver()
    driver.set_window_size(1024, 768)
    driver.implicitly_wait(0.5)
    yield driver
    driver.quit()