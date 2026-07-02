from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from utils.config.config_manager import ConfigManager
from web_driver.driver import Driver
import logging

logger = logging.getLogger(__name__)

class Alert:
    def __init__(self) -> None:
        try:
            logger.info("Ждём переключения на алерт")
            self._instance = WebDriverWait(
                driver=Driver().get_driver(), timeout=ConfigManager().instance().timeout
            ).until(lambda d : d.switch_to.alert)
        except TimeoutException:
            logger.error("Алерт не появился")
            raise

    def get_alert_text(self) -> str:
        logger.info(f"Получаем текст алерта")
        text = self._instance.text
        return text


    def accept_alert(self) -> None:
        logger.info(f"Принимаем алерт")
        self._instance.accept()