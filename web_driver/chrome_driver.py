from selenium import webdriver
from selenium.webdriver.common.options import ArgOptions

from utils.config.config_manager import ConfigManager
from web_driver.base_driver import BaseDriver

import logging
logger = logging.getLogger(__name__)


class ChromeDriver(BaseDriver):
    def __init__(self) -> None:
        super().__init__()
        options = self._set_options()
        logger.info("Создаём драйвер Chrome")
        self._driver = webdriver.Chrome(options=options)

    @staticmethod
    def _set_options() -> ArgOptions:
        options = webdriver.ChromeOptions()
        for arg in ConfigManager().instance().chrome_driver_args:
            options.add_argument(arg)
        return options
