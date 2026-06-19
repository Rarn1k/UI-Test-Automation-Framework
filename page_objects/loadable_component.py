from abc import ABC, abstractmethod


class LoadableComponent(ABC):
    @abstractmethod
    def _load(self) -> None:
        pass

    @abstractmethod
    def _is_loaded(self) -> bool:
        pass

    def get(self):
        if not self._is_loaded():
            self._load()
        if not self._is_loaded():
            raise Exception("Page not loaded properly.")
        return self
