from selenium.webdriver.common.by import By

from element_objects.label import Label
from page_objects.base_page import BasePage


class SamplePage(BasePage):
    def __init__(self) -> None:
        element = Label((By.ID, "sampleHeading"), "Sample heading")
        super().__init__(element, "Sample page")
