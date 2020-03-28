import datetime
from dataclasses import dataclass, field
from typing import List

from taiken_ddd.src.v4.domain.interview_v4 import InterviewV4


@dataclass(frozen=True)
class Interviews:
    values: List[InterviewV4] = field(default_factory=list)

    def add_next_interview(self, interview_date: datetime.date) -> None:
        interview = InterviewV4(interview_date, self.next_interview_number())

        self.values.append(interview)

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, index: int) -> InterviewV4:
        return self.values[index]

    def next_interview_number(self) -> int:
        return len(self.values) + 1
