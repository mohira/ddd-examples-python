from abc import ABCMeta, abstractmethod

from taiken_ddd.src.v3.domain.screening_v3 import ScreeningV3


class ScreeningRepository(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, screening: ScreeningV3) -> None:
        pass

    @abstractmethod
    def find_by_id(self, screening_id: str) -> ScreeningV3:
        pass

    @abstractmethod
    def update(self, screening: ScreeningV3) -> None:
        pass
