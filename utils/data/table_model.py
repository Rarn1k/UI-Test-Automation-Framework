from dataclasses import dataclass

@dataclass
class TableModel:
    first_name: str
    last_name: str
    age: int
    email: str
    salary: int
    department: str