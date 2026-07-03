import logging

from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.frames.bottom_frame_page import BottomFramePage
from page_objects.frames.frames_page import FramesPage
from page_objects.frames.upper_frame_page import UpperFramePage
from page_objects.left_menu_page import LeftMenuPage
from page_objects.main_page import MainPage
from page_objects.frames.nested_frames.child_iframe import ChildIFramePage
from page_objects.frames.nested_frames.nested_frames_page import NestedFramesPage
from page_objects.frames.nested_frames.parent_frame_page import ParentFramePage

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
    nested_frames = NestedFramesPage()
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
    child_frame.switch_to_default()

    logger.info("Нажимаем на ссылку Frames")
    left_menu.click_frames()
    logger.info("Создаём экземпляр страницы Frames")
    frames = FramesPage()
    logger.info("Проверяем, что открылась страница Frames")
    assert frames.is_displayed(), "Страница Frames не отобразилась"
    logger.info("Переключаемся на верхний фрейм")
    frames.switch_to_upper_frame()
    logger.info("Создаём экземпляр страницы верхнего фрейма")
    upper_frame = UpperFramePage()
    logger.info("Проверяем, что открылась страница верхнего фрейма")
    assert upper_frame.is_displayed(), "Страница upper_frame не отобразилась"
    logger.info("Получаем надпись со страницы верхнего фрейма")
    upper_frame_text = upper_frame.get_page_text()
    logger.info("Переключаемся на обычную страницу")
    upper_frame.switch_to_default()
    logger.info("Переключаемся на нижний фрейм")
    frames.switch_to_bottom_frame()
    logger.info("Создаём экземпляр страницы нижнего фрейма")
    bottom_frame = BottomFramePage()
    logger.info("Проверяем, что открылась страница нижнего фрейма")
    assert bottom_frame.is_displayed(), "Страница bottom_frame не отобразилась"
    logger.info("Получаем надпись со страницы нижнего фрейма")
    bottom_frame_text = upper_frame.get_page_text()
    logger.info("Проверяем, что надпись из верхнего фрейма соответствует надписи из нижнего")
    assert upper_frame_text == bottom_frame_text, \
        f"Надпись из верхнего фрейма: {upper_frame_text} не соответствует надписи из нижнего: {bottom_frame_text}"
