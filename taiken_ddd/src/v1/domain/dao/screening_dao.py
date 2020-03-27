from taiken_ddd.src.v1.domain.screening_v1 import ScreeningV1


class ScreeningDao:
    def insert(self, screening: ScreeningV1) -> None:
        # INSERT文省略
        pass

    def find_screening_by_id(self, screening_id: str) -> ScreeningV1:
        # SELECT文省略
        pass
