from utils.data.data_model import DataModel
from utils.file_data_reader import FileDataReader
from utils.get_project_path import ProjectPath
from utils.singleton_meta import SingletonMeta


class DataManager(metaclass=SingletonMeta):
    _instance: DataModel = None
    _data_path = ProjectPath.get_root() / "utils" / "data" / "data.json"

    def __init__(self) -> None:
        self._instance = FileDataReader.read_and_parse(str(self._data_path), DataModel)

    def instance(self) -> DataModel:
        if self._instance is None:
            raise RuntimeError("DataManager не инициализирован")
        return self._instance