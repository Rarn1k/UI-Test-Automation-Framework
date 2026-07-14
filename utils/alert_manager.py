from utils.logger_manager import LoggerManager
from utils.waiter import Waiter


class AlertManager:
    @staticmethod
    def get_alert_text() -> str:
        LoggerManager().info("Ждём переключения на алерт")
        alert = Waiter.wait_for_alert()
        LoggerManager().info(f"Получаем текст алерта")
        return alert.text

    @staticmethod
    def accept_alert() -> None:
        LoggerManager().info("Ждём переключения на алерт")
        alert = Waiter.wait_for_alert()
        LoggerManager().info(f"Принимаем алерт")
        alert.accept()

    @staticmethod
    def wait_alert_closed() -> bool:
        LoggerManager().info("Ждём, пока алерт закроется")
        return Waiter.wait_until_alert_closed()

    @staticmethod
    def send_keys(text: str) -> None:
        LoggerManager().info("Ждём переключения на алерт")
        alert = Waiter.wait_for_alert()
        LoggerManager().info(f"Вводим текст в алерт: '{text}'")
        alert.send_keys(text)
