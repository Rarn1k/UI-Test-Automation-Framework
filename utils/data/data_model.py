from dataclasses import dataclass

@dataclass
class DataModel:
    alert_text: str
    confirm_text: str
    confirm_result_text: str