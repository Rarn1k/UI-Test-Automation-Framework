from dataclasses import dataclass

from utils.data.table_model import TableModel


@dataclass
class DataModel:
    alert_text: str
    confirm_text: str
    confirm_result_text: str
    prompt_text: str
    prompt_result_text: str

    table_users: list[TableModel]

    def __post_init__(self):
        self.table_users = [TableModel(**user) if isinstance(user, dict) else user for user in self.table_users]
