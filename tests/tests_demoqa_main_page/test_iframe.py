from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.frames.frames_page import FramesPage
from page_objects.left_menu_page import LeftMenuPage
from page_objects.main_page import MainPage
from page_objects.nested_frames.nested_frames_page import NestedFramesPage
from utils.logger_manager import LoggerManager


def test_iframes(driver: WebDriver, main_page: MainPage) -> None:
    LoggerManager().info("Проверяем, что главная страница не отобразилась")
    assert main_page.is_displayed(), "Главная страница не отобразилась"

    LoggerManager().info("Нажимаем на ссылку alerts, frame & Windows")
    main_page.click_alerts_windows()
    LoggerManager().info("Создаём экземпляр страницы левого меню")
    left_menu = LeftMenuPage()
    LoggerManager().info("Проверяем, что открылось левое меню")
    assert left_menu.is_displayed(), "Левое меню не отобразилось"
    LoggerManager().info("Нажимаем на ссылку Nested Frames")
    left_menu.click_nested_frames()
    LoggerManager().info("Создаём экземпляр страницы Nested Frames")
    nested_frames = NestedFramesPage()
    LoggerManager().info("Проверяем, что открылась страница Nested Frames")
    assert nested_frames.is_displayed(), "Страница Nested Frames не отобразилась"
    LoggerManager().info("Проверяем, что присутствует надпись: Parent frame")
    assert nested_frames.get_parent_frame_text() == "Parent frame", "Отсутствует надпись: Parent frame"
    LoggerManager().info("Проверяем, что присутствует надпись: Child frame")
    assert nested_frames.get_child_frame_text() == "Child Iframe", "Отсутствует надпись: Child frame"

    LoggerManager().info("Нажимаем на ссылку Frames")
    left_menu.click_frames()
    LoggerManager().info("Создаём экземпляр страницы Frames")
    frames = FramesPage()
    LoggerManager().info("Проверяем, что открылась страница Frames")
    assert frames.is_displayed(), "Страница Frames не отобразилась"
    LoggerManager().info("Получаем надпись со страницы верхнего фрейма")
    upper_frame_text = frames.get_upper_frame_text()
    LoggerManager().info("Получаем надпись со страницы нижнего фрейма")
    bottom_frame_text = frames.get_bottom_frame_text()
    LoggerManager().info("Проверяем, что надпись из верхнего фрейма соответствует надписи из нижнего")
    assert upper_frame_text == bottom_frame_text, \
        f"Надпись из верхнего фрейма: {upper_frame_text} не соответствует надписи из нижнего: {bottom_frame_text}"
