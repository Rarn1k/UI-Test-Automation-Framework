import json
from typing import TypeVar, Type

T = TypeVar('T')

class FileDataReader:
    @staticmethod
    def read_and_parse(file_path: str, model_class: Type[T]) -> T:
        with open(file_path, 'r', encoding='utf-8') as f:
            raw_data = json.load(f)
        return model_class(**raw_data)