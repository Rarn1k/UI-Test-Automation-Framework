from utils.data.data_model import DataModel
from utils.file_data_reader import FileDataReader
from utils.singleton_meta import SingletonMeta


class DataProvider(metaclass=SingletonMeta):
    _instance: DataModel = None
    _config_path = "./utils/data/data.json"

    def __init__(self) -> None:
        self._instance = FileDataReader.read_and_parse(self._config_path, DataModel)

    def instance(self) -> DataModel:
        if self._instance is None:
            raise RuntimeError("ConfigProvider не инициализирован")
        return self._instance