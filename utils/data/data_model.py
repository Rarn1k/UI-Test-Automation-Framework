from dataclasses import dataclass

@dataclass
class DataModel:
    filters: dict[str, list[str]]
