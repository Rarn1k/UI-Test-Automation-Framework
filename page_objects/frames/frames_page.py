from selenium.webdriver.common.by import By

from element_objects.label import Label
from page_objects.base_page import BasePage
from page_objects.frames.bottom_frame_page import BottomFramePage
from page_objects.frames.upper_frame_page import UpperFramePage
from utils.frame_manager import FrameManager
from utils.logger_manager import LoggerManager


class FramesPage(BasePage):
    __upper_frame = Label((By.ID, "frame1"), "Upper frame")
    __bottom_frame = Label((By.ID, "frame2"), "Bottom frame")

    def __init__(self) -> None:
        element = Label((By.XPATH, "//*[@class='text-center' and text()='Frames']"), "Frames")
        super().__init__(element, "Frames page")

    def get_upper_frame_text(self) -> str:
        with FrameManager.frame_context(self.__upper_frame):
            LoggerManager().info("Получаем верхний фрейм")
            upper_page = UpperFramePage()
            return upper_page.get_page_text()

    def get_bottom_frame_text(self) -> str:
        with FrameManager.frame_context(self.__bottom_frame):
            LoggerManager().info("Получаем нижний фрейм")
            bottom_page = BottomFramePage()
            return bottom_page.get_page_text()
