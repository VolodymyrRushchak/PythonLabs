from abc import ABC, abstractmethod


class Figure2D(ABC):
    @property
    @abstractmethod
    def area(self) -> float:
        pass
