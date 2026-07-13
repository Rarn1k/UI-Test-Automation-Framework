import logging

from utils.path_utils import PathUtils
from utils.singleton_meta import SingletonMeta

class LoggerManager(metaclass=SingletonMeta):
    def __init__(self):
        self._logger = logging.getLogger("DemoqaLogger")
        self._setup_logger()

    def _setup_logger(self) -> None:
        self._logger.setLevel(logging.INFO)

        log_path = PathUtils.get_logs()
        log_path.parent.mkdir(parents=True, exist_ok=True)

        formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)

        self._logger.addHandler(handler)

    def get_logger(self) -> logging.Logger:
        return self._logger
