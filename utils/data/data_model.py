from dataclasses import dataclass

@dataclass
class DataModel:
    filters: dict[str, list[str]]
    first_game_attrs: list[str]