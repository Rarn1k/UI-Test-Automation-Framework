from pathlib import Path


class GetMarkerPath:
    @staticmethod
    def get_marker_path(marker: str = "requirements.txt") -> Path:
        current = Path(__file__).resolve()
        for parent in current.parents:
            if (parent / marker).exists():
                return parent
        raise FileNotFoundError(f"Не найден маркер {marker} в родительских директориях")
