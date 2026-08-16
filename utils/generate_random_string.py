import random
import string

from utils.logger_manager import LoggerManager

class RandomUtils:
    DEFAULT_LENGTH : int = 10

    @classmethod
    def generate_random_string(cls, length: int = DEFAULT_LENGTH) -> str:
        LoggerManager().info("Создаём случайную строку")
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))