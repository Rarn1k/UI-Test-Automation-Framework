from pathlib import Path


class PathUtils:
    @staticmethod
    def get_project_root(marker: str = "requirements.txt") -> Path:
        current = Path(__file__).resolve()
        for parent in current.parents:
            if (parent / marker).exists():
                return parent
        raise FileNotFoundError(f"Не найден маркер {marker} в родительских директориях")

    @classmethod
    def get_resources(cls) -> Path:
        return cls.get_project_root() / "utils" / "data" / "data.json"

    @classmethod
    def get_config(cls) -> Path:
        return cls.get_project_root() / "utils" / "config" / "config.json"

    @classmethod
    def get_logs(cls) -> Path:
        return cls.get_project_root() / "logs" / "test.log"
