import random
import string

from utils.logger_manager import LoggerManager


def generate_random_string(length: int = 10) -> str:
    LoggerManager().get_logger().info("Создаём случайную строку")
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))