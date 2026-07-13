from selenium.webdriver.common.by import By

from element_objects.button import Button
from element_objects.input import Input
from element_objects.label import Label
from page_objects.base_page import BasePage
from utils.data.table_model import TableModel
from utils.logger_manager import LoggerManager


class RegistrationFormPage(BasePage):
    __first_name_input = Input((By.ID, 'firstName'), "First name input")
    __last_name_input = Input((By.ID, 'lastName'), "Last name input")
    __email_input = Input((By.ID, 'userEmail'), "Email input")
    __age_input = Input((By.ID, 'age'), "Age input")
    __salary_input = Input((By.ID, 'salary'), "Salary input")
    __department_input = Input((By.ID, 'department'), "Department input")

    __submit_button = Button((By.ID, 'submit'), 'Submit button')

    def __init__(self) -> None:
        super().__init__((By.ID, "registration-form-modal"), "Registration form")

    def is_displayed(self) -> bool:
        LoggerManager().get_logger().info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def set_all_inputs(self, user: TableModel) -> None:
        self.set_first_name(user.first_name)
        self.set_last_name(user.last_name)
        self.set_email(user.email)
        self.set_age(user.age)
        self.set_salary(user.salary)
        self.set_department(user.department)

    def set_first_name(self, first_name: str) -> None:
        LoggerManager().get_logger().info(f"Заполняем имя значением: {first_name}")
        self.__first_name_input.set_value(first_name)

    def set_last_name(self, last_name: str) -> None:
        LoggerManager().get_logger().info(f"Заполняем фамилию значением: {last_name}")
        self.__last_name_input.set_value(last_name)

    def set_email(self, email: str) -> None:
        LoggerManager().get_logger().info(f"Заполняем почту значением: {email}")
        self.__email_input.set_value(email)

    def set_age(self, age: str) -> None:
        LoggerManager().get_logger().info(f"Заполняем возраст значением: {age}")
        self.__age_input.set_value(age)

    def set_salary(self, salary: str) -> None:
        LoggerManager().get_logger().info(f"Заполняем зарплату значением: {salary}")
        self.__salary_input.set_value(salary)

    def set_department(self, department: str) -> None:
        LoggerManager().get_logger().info(f"Заполняем департамент значением: {department}")
        self.__department_input.set_value(department)

    def click_submit(self) -> None:
        LoggerManager().get_logger().info(f"Отправляем введённые данные")
        self.__submit_button.click()

    def is_not_displayed(self) -> bool:
        LoggerManager().get_logger().info(f"Проверяем, что страница {self._name} закрылась")
        return Label(self._locator, self._name).wait_closed()
