from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from element_objects.label import Label
from page_objects.base_page import BasePage
from utils.data.table_model import TableModel
from utils.logger_manager import LoggerManager


class TablePage(BasePage):
    __table_header = Label((By.XPATH, "//thead//th"), "Table header")
    __table_row = Label((By.XPATH, "//tbody//tr"), "Table row")
    __table_cell = Label((By.XPATH, ".//td"), "Table cell")
    __delete_row_button = Label((By.XPATH, ".//*[@title='Delete']"), "Delete table")

    def __init__(self):
        super().__init__((By.XPATH, "//table[contains(@class, 'table')]"), "Table page")

    def is_displayed(self) -> bool:
        LoggerManager().info(f"Проверяем, загружена ли страница таблицы {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def get_rows(self) -> list[WebElement]:
        LoggerManager().info("Ищем строки таблицы")
        return self.__table_row.find_elements()

    def _parse_row_to_model(self, row: WebElement, headers_by_index: dict) -> TableModel:
        LoggerManager().info("Преобразуем строку таблицы в объект TableModel.")
        cells_texts = self.__table_cell.get_texts(row)
        return TableModel(
            first_name=cells_texts[headers_by_index["First Name"]],
            last_name=cells_texts[headers_by_index["Last Name"]],
            age=cells_texts[headers_by_index["Age"]],
            email=cells_texts[headers_by_index["Email"]],
            salary=cells_texts[headers_by_index["Salary"]],
            department=cells_texts[headers_by_index["Department"]]
        )

    def _get_headers_by_index(self) -> dict:
        return {header: idx for idx, header in enumerate(self.__table_header.get_texts())}

    def get_all_data(self) -> list[TableModel]:
        LoggerManager().info("Собираем всю информацию с таблицы")
        rows = self.get_rows()
        return [self._parse_row_to_model(row, self._get_headers_by_index()) for row in rows]

    def find_row_by_data(self, data: TableModel) -> WebElement | None:
        LoggerManager().info(f"Ищем строку по данным: {data}")
        rows = self.get_rows()
        for row in rows:
            model = self._parse_row_to_model(row, self._get_headers_by_index())
            if model == data:
                return row
        LoggerManager().warning(f"Строка с данными {data} не найдена")
        return None

    def is_data_in_table(self, data: TableModel) -> bool:
        LoggerManager().info(f"Проверяем, что {data} есть в таблице")
        return data in self.get_all_data()

    def delete_row(self, row: WebElement):
        LoggerManager().info(f"Удаляем строку{row}")
        self.__delete_row_button.find_element(row).click()
