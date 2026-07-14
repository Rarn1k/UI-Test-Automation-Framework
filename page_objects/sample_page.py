from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class SamplePage(BasePage):
    def __init__(self) -> None:
        super().__init__((By.ID, "sampleHeading"), "Sample page")
