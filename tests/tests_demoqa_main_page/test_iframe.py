import logging

from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.left_menu_page import LeftMenuPage
from page_objects.main_page import MainPage
from page_objects.nested_frames.child_iframe import ChildIFramePage
from page_objects.nested_frames.nested_frames_page import NestedFrames
from page_objects.nested_frames.parent_frame_page import ParentFramePage
from web_driver.driver import Driver

logger = logging.getLogger(__name__)


def test_alerts(driver: WebDriver, main_page: MainPage) -> None:
    logger.info("Проверяем, что главная страница не отобразилась")
    assert main_page.is_displayed(), "Главная страница не отобразилась"

    logger.info("Нажимаем на ссылку alerts, frame & Windows")
    main_page.click_alerts_windows()
    logger.info("Создаём экземпляр страницы левого меню")
    left_menu = LeftMenuPage()
    logger.info("Проверяем, что открылось левое меню")
    assert left_menu.is_displayed(), "Левое меню не отобразилось"
    logger.info("Нажимаем на ссылку Nested Frames")
    left_menu.click_nested_frames()
    logger.info("Создаём экземпляр страницы Nested Frames")
    nested_frames = NestedFrames()
    logger.info("Проверяем, что открылась страница Nested Frames")
    assert nested_frames.is_displayed(), "Страница Nested Frames не отобразилась"
    logger.info("Переключаемся на родительский фрейм")
    nested_frames.switch_to_parent_frame()
    logger.info("Создаём экземпляр страницы родительского фрейма")
    parent_frame = ParentFramePage()
    logger.info("Проверяем, что открылась страница родительского фрейма")
    assert parent_frame.is_displayed(), "Страница parent_frame не отобразилась"
    logger.info("Проверяем, что присутствует надпись: Parent frame")
    assert parent_frame.get_page_text() == "Parent frame", "Отсутствует надпись: Parent frame"
    logger.info("Переключаемся на дочерний фрейм")
    parent_frame.switch_to_child_frame()
    logger.info("Создаём экземпляр страницы дочернего фрейма")
    child_frame = ChildIFramePage()
    logger.info("Проверяем, что открылась страница дочернего фрейма")
    assert child_frame.is_displayed(), "Страница child_frame не отобразилась"
    logger.info("Проверяем, что присутствует надпись: Child frame")
    assert child_frame.get_page_text() == "Child Iframe", "Отсутствует надпись: Child frame"
    logger.info("Переключаемся на обычную страницу")
    Driver().get_driver().switch_to.default_content()