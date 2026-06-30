from dataclasses import dataclass

@dataclass
class ConfigModel:
    demoqa_url: str
    browser: str
    timeout: int
    chrome_driver_args: list[str]
    firefox_driver_args: list[str]