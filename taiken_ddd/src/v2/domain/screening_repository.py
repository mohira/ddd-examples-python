from abc import ABCMeta, abstractmethod

from taiken_ddd.src.v2.domain.screening_v2 import ScreeningV2


class ScreeningRepository(metaclass=ABCMeta):
    @abstractmethod
    def insert(self, screening: ScreeningV2) -> None:
        pass

    @abstractmethod
    def find_by_id(self, screening_id: str) -> ScreeningV2:
        pass

    @abstractmethod
    def update(self, screening: ScreeningV2) -> None:
        pass
