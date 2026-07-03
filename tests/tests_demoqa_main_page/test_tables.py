import logging
import pytest

from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.left_menu_page import LeftMenuPage
from page_objects.main_page import MainPage
from page_objects.registration_form_page import RegistrationFormPage
from page_objects.web_tables_page import WebTablesPage
from utils.data.data_manager import DataManager
from utils.data.table_model import TableModel

logger = logging.getLogger(__name__)

@pytest.mark.parametrize("user", DataManager().instance().table_users)
def test_alerts(driver: WebDriver, main_page: MainPage, user: TableModel) -> None:
    logger.info("Проверяем, что главная страница не отобразилась")
    assert main_page.is_displayed(), "Главная страница не отобразилась"

    logger.info("Нажимаем на кнопку Elements")
    main_page.click_elements()
    logger.info("Создаём экземпляр страницы левого меню")
    left_menu = LeftMenuPage()
    logger.info("Проверяем, что открылось левое меню")
    assert left_menu.is_displayed(), "Левое меню не отобразилось"
    logger.info("Нажимаем на ссылку Web Tables")
    left_menu.click_web_tables()
    logger.info("Создаём экземпляр страницы Web Tables")
    web_tables_page = WebTablesPage()
    logger.info("Проверяем, что открылась страница Web Tables")
    assert web_tables_page.is_displayed(), "Страница Web Tables не отобразилась"

    logger.info("Нажимаем на кнопку добавления новой записи")
    web_tables_page.click_add_new_record()
    logger.info("Создаём экземпляр страницы формы регистрации")
    registration = RegistrationFormPage()
    logger.info("Проверяем, что открылась страница формы регистрации")
    assert registration.is_displayed(), "Страница формы регистрации не отобразилась"

    logger.info(f"Вводим все данные пользователя {user}")
    registration.set_all_inputs(user)
    logger.info("Нажимаем кнопку Submit")
    registration.click_submit()
    logger.info("Ожидаем, что страница форма регистрации закрылась")
    assert registration.is_not_displayed(), "Страница формы регистрации не закрылась"
