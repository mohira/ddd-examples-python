from typing import List

from taiken_ddd.src.v1.domain.interview_v1 import InterviewV1


class InterviewDao:
    def find_by_screening_id(self, screening_id: str) -> List[InterviewV1]:
        # SELECT文省略
        pass

    def insert(self, interview: InterviewV1) -> None:
        # INSERT文省略
        pass
