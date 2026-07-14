import pytest

from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.left_menu_page import LeftMenuPage
from page_objects.main_page import MainPage
from page_objects.registration_form_page import RegistrationFormPage
from page_objects.table_page import TablePage
from page_objects.web_tables_page import WebTablesPage
from utils.data.data_manager import DataManager
from utils.data.table_model import TableModel
from utils.logger_manager import LoggerManager


@pytest.mark.parametrize("user", DataManager().instance().table_users)
def test_table(driver: WebDriver, main_page: MainPage, user: TableModel) -> None:
    LoggerManager().info("Проверяем, что главная страница не отобразилась")
    assert main_page.is_displayed(), "Главная страница не отобразилась"

    LoggerManager().info("Нажимаем на кнопку Elements")
    main_page.click_elements()
    LoggerManager().info("Создаём экземпляр страницы левого меню")
    left_menu = LeftMenuPage()
    LoggerManager().info("Проверяем, что открылось левое меню")
    assert left_menu.is_displayed(), "Левое меню не отобразилось"
    LoggerManager().info("Нажимаем на ссылку Web Tables")
    left_menu.click_web_tables()
    LoggerManager().info("Создаём экземпляр страницы Web Tables")
    web_tables_page = WebTablesPage()
    LoggerManager().info("Проверяем, что открылась страница Web Tables")
    assert web_tables_page.is_displayed(), "Страница Web Tables не отобразилась"

    LoggerManager().info("Нажимаем на кнопку добавления новой записи")
    web_tables_page.click_add_new_record()
    LoggerManager().info("Создаём экземпляр страницы формы регистрации")
    registration = RegistrationFormPage()
    LoggerManager().info("Проверяем, что открылась страница формы регистрации")
    assert registration.is_displayed(), "Страница формы регистрации не отобразилась"

    LoggerManager().info(f"Вводим все данные пользователя {user}")
    registration.set_all_inputs(user)
    LoggerManager().info("Нажимаем кнопку Submit")
    registration.click_submit()
    LoggerManager().info("Ожидаем, что страница форма регистрации закрылась")
    assert registration.is_not_displayed(), "Страница формы регистрации не закрылась"
    LoggerManager().info("Создаём экземпляр страницы таблицы")
    table = TablePage()
    LoggerManager().info("Проверяем, что таблица появилась")
    assert table.is_displayed(), "Таблица не отобразилась"
    LoggerManager().info(f"Проверяем, что данные пользователя {user} появились в таблице")
    LoggerManager().info(f"{table.get_all_data()}")
    assert table.is_data_in_table(user), f"Данные пользователя {user} не появились в таблице"

    LoggerManager().info("Получаем количество записей до удаления")
    row_count_before = len(table.get_rows())
    LoggerManager().info(f"Получаем строку с пользователем {user}")
    user_row = table.find_row_by_data(user)
    LoggerManager().info(f"Нажимаем кнопку Delete в строке пользователя {user}")
    table.delete_row(user_row)
    LoggerManager().info("Получаем количество записей после удаления")
    row_count_after = len(table.get_rows())
    LoggerManager().info("Проверяем, что количество записей в таблице изменилось")
    assert row_count_before != row_count_after, f"Количество записей в таблице не изменилось: {row_count_before}"
    LoggerManager().info(f"Проверяем, что пользователь {user} удалился из таблицы")
    assert not table.find_row_by_data(user), f"Пользователь {user} не удалился из таблицы"
