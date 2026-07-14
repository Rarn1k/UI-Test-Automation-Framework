import logging

from utils.path_utils import PathUtils
from utils.singleton_meta import SingletonMeta

class LoggerManager(metaclass=SingletonMeta):
    LOGGER_NAME = "demoqa_logger"
    LOG_LEVEL = logging.INFO

    def __init__(self):
        self._logger = logging.getLogger(self.LOGGER_NAME)
        self._setup_logger()

    def _setup_logger(self) -> None:
        self._logger.setLevel(logging.INFO)

        formatter = logging.Formatter(
            fmt="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        self._add_file_handler(formatter)


    def _add_file_handler(self, formatter: logging.Formatter) -> None:
        log_path = PathUtils.get_logs()
        log_path.parent.mkdir(parents=True, exist_ok=True)

        handler = logging.FileHandler(log_path, mode="w", encoding="utf-8")
        handler.setLevel(logging.INFO)
        handler.setFormatter(formatter)

        self._logger.addHandler(handler)

    def info(self, message: str) -> None:
        self._logger.info(message, stacklevel=2)

    def warning(self, message: str) -> None:
        self._logger.warning(message, stacklevel=2)

    def error(self, message: str) -> None:
        self._logger.error(message, stacklevel=2)

    def debug(self, message: str) -> None:
        self._logger.debug(message, stacklevel=2)