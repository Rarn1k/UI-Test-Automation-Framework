from dataclasses import dataclass

@dataclass
class ConfigModel:
    steam_url: str
    timeout: int
    driver_window_width: int
    driver_window_height: int
    driver_implicitly_wait: float
    driver_args: list[str]