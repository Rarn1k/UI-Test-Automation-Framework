from selenium.webdriver.common.by import By

from element_objects.label import Label
from page_objects.base_page import BasePage
from page_objects.nested_frames.child_iframe import ChildIFramePage
from page_objects.nested_frames.parent_frame_page import ParentFramePage
from utils.frame_manager import FrameManager
from utils.logger_manager import LoggerManager


class NestedFramesPage(BasePage):
    __parent_frame = Label((By.ID, "frame1"), "Parent frame")
    __child_frame = Label((By.XPATH, "//iframe[contains(@srcdoc, 'Child Iframe')]"), "Child Iframe")

    def __init__(self) -> None:
        super().__init__((By.XPATH, "//*[@class='text-center' and text()='Nested Frames']"),
                         "Nested frames page")

    def is_displayed(self) -> bool:
        LoggerManager().get_logger().info(f"Проверяем, загружена ли страница {self._name}")
        return Label(self._locator, self._name).find_element().is_displayed()

    def get_parent_frame_text(self) -> str:
        LoggerManager().get_logger().info(f"Получаем текст родительского фрейма")
        with FrameManager.frame_context(self.__parent_frame):
            parent_page = ParentFramePage()
            return parent_page.get_page_text()

    def get_child_frame_text(self) -> str:
        LoggerManager().get_logger().info(f"Получаем текст дочернего фрейма")
        with FrameManager.frame_context(self.__parent_frame):
            with FrameManager.frame_context(self.__child_frame):
                child_page = ChildIFramePage()
                return child_page.get_page_text()
