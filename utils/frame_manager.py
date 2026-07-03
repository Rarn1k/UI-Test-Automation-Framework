from selenium.webdriver.remote.webelement import WebElement

from web_driver.driver import Driver


class FrameManager:
    @staticmethod
    def switch_to_frame(frame: WebElement) -> None:
        Driver().get_driver().switch_to.frame(frame)

    @staticmethod
    def switch_to_default() -> None:
        Driver().get_driver().switch_to.default_content()