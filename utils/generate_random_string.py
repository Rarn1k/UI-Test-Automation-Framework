import random
import string
import logging

logger = logging.getLogger(__name__)


def generate_random_string(length: int = 10) -> str:
    logger.info("Создаём случайную строку")
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))