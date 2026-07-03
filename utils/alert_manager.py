from utils.waiter import Waiter
import logging

logger = logging.getLogger(__name__)


class AlertManager:
    def __init__(self) -> None:
        self._waiter = Waiter()
        logger.info("Ждём переключения на алерт")
        self._instance = self._waiter.wait_for_alert()

    def get_alert_text(self) -> str:
        logger.info(f"Получаем текст алерта")
        text = self._instance.text
        return text

    def accept_alert(self) -> None:
        logger.info(f"Принимаем алерт")
        self._instance.accept()

    def wait_alert_closed(self) -> bool:
        logger.info("Ждём, пока алерт закроется")
        return self._waiter.wait_until_alert_closed()

    def send_keys(self, text: str) -> None:
        logger.info(f"Вводим текст в алерт: '{text}'")
        self._instance.send_keys(text)