from selenium.webdriver.common.by import By

from page_objects.base_page import BasePage


class AboutPage(BasePage):

    @property
    def _main_by(self):
        return By.ID, "about_header_area"
