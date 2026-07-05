from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from element_objects.label import Label
from page_objects.base_page import BasePage
import logging

from utils.data.table_model import TableModel

logger = logging.getLogger(__name__)

class TablePage(BasePage):
    __table_header = Label((By.XPATH, "//thead//th"), "Table header")
    __table_row = Label((By.XPATH, "//tbody//tr"), "Table row")
    __table_cell = Label((By.XPATH, ".//td"), "Table cell")

    def __init__(self):
        super().__init__((By.XPATH, "//table[contains(@class, 'table')]"), "Table page")

    def is_displayed(self) -> bool:
        logger.info(f"Проверяем, загружена ли страница таблицы {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def get_rows(self) -> list[WebElement]:
        logger.info("Ищем строки таблицы")
        return self.__table_row.find_elements()

    def get_all_data(self) -> list[TableModel]:
        logger.info("Собираем всю информацию с таблицы")
        headers_by_index = {header: idx for idx, header in enumerate(self.__table_header.get_texts())}
        rows = self.get_rows()
        result = []
        for row in rows:
            cells_texts = self.__table_cell.get_texts(row)
            result.append(
                TableModel(
                    first_name=cells_texts[headers_by_index["First Name"]],
                    last_name=cells_texts[headers_by_index["Last Name"]],
                    age=cells_texts[headers_by_index["Age"]],
                    email=cells_texts[headers_by_index["Email"]],
                    salary=cells_texts[headers_by_index["Salary"]],
                    department=cells_texts[headers_by_index["Department"]]
                )
            )
        return result

    def is_data_in_table(self, data: TableModel) -> bool:
        logger.info(f"Проверяем, что {data} есть в таблице")
        return data in self.get_all_data()
