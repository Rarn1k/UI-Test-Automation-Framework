from selenium.common import TimeoutException
from selenium.webdriver.common.by import By

from page_objects.action_bot import ActionBot
from page_objects.base_page import BasePage


class AboutPage(BasePage):
    _main_by = By.ID, "about_header_area"
