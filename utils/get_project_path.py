from pathlib import Path


class ProjectPath:
    @staticmethod
    def get_root(marker: str = "requirements.txt") -> Path:
        current = Path(__file__).resolve()
        for parent in current.parents:
            if (parent / marker).exists():
                return parent
        raise FileNotFoundError(f"Не найден маркер {marker} в родительских директориях")
