from dataclasses import dataclass

from utils.data.user_model import User


@dataclass
class DataModel:
    alert_text: str
    confirm_text: str
    confirm_result_text: str
    prompt_text: str
    prompt_result_text: str

    table_users: list[User]

    def __post_init__(self):
        self.table_users = [User(**user) if isinstance(user, dict) else user for user in self.table_users]
