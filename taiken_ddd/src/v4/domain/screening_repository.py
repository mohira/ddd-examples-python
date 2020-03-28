from abc import ABCMeta, abstractmethod

from taiken_ddd.src.v4.domain.screening_v4 import ScreeningV4


class ScreeningRepository(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, screening: ScreeningV4) -> None:
        pass

    @abstractmethod
    def find_by_id(self, screening_id: str) -> ScreeningV4:
        pass

    @abstractmethod
    def update(self, screening: ScreeningV4) -> None:
        pass
