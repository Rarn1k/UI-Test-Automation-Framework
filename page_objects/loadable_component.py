from abc import ABC, abstractmethod


class LoadableComponent(ABC):
    @abstractmethod
    def load(self) -> None:
        pass

    @abstractmethod
    def is_loaded(self) -> bool:
        pass

    def get(self):
        if not self.is_loaded():
            self.load()
        if not self.is_loaded():
            raise Exception("Page not loaded properly.")
        return self
