from utils.config.config_model import ConfigModel
from utils.file_data_reader import FileDataReader
from utils.path_utils import PathUtils
from utils.singleton_meta import SingletonMeta


class ConfigManager(metaclass=SingletonMeta):
    _instance: ConfigModel = None
    _config_path = PathUtils.get_config()

    def __init__(self) -> None:
        self._instance = FileDataReader.read_and_parse(str(self._config_path), ConfigModel)

    def instance(self) -> ConfigModel:
        if self._instance is None:
            raise RuntimeError("ConfigProvider не инициализирован")
        return self._instance