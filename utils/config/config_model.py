from dataclasses import dataclass

@dataclass
class ConfigModel:
    steam_url: str
    use_incognito: bool
    timeout: int