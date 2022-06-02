from abc import ABC, abstractmethod


class Figure3D(ABC):
    @property
    @abstractmethod
    def volume(self) -> float:
        pass

    @property
    @abstractmethod
    def surface_area(self) -> float:
        pass
