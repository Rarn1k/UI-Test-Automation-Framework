from selenium.webdriver.common.by import By

from element_objects.label import Label
from page_objects.base_page import BasePage


class RegistrationFormPage(BasePage):
    def __init__(self):
        super().__init__((By.ID, "registration-form-modal"), "Registration form")

    def is_displayed(self) -> bool:
        return Label(self._locator, self._name).find_element().is_displayed()

    