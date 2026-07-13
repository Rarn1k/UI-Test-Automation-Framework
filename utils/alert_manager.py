from utils.logger_manager import LoggerManager
from utils.waiter import Waiter


class AlertManager:
    @staticmethod
    def get_alert_text() -> str:
        LoggerManager().get_logger().info("Ждём переключения на алерт")
        alert = Waiter.wait_for_alert()
        LoggerManager().get_logger().info(f"Получаем текст алерта")
        return alert.text

    @staticmethod
    def accept_alert() -> None:
        LoggerManager().get_logger().info("Ждём переключения на алерт")
        alert = Waiter.wait_for_alert()
        LoggerManager().get_logger().info(f"Принимаем алерт")
        alert.accept()

    @staticmethod
    def wait_alert_closed() -> bool:
        LoggerManager().get_logger().info("Ждём, пока алерт закроется")
        return Waiter.wait_until_alert_closed()

    @staticmethod
    def send_keys(text: str) -> None:
        LoggerManager().get_logger().info("Ждём переключения на алерт")
        alert = Waiter.wait_for_alert()
        LoggerManager().get_logger().info(f"Вводим текст в алерт: '{text}'")
        alert.send_keys(text)
