from __future__ import annotations

import datetime
from dataclasses import dataclass, field
from typing import List

from taiken_ddd.src.v3.domain.interview_v3 import InterviewV3


# 外部での Interviews.values.append() は防げないので注意
@dataclass(frozen=True)
class Interviews:
    values: List[InterviewV3] = field(default_factory=list)

    def add_next_interview(self, interview_date: datetime.date) -> None:
        interview = InterviewV3(interview_date, self.next_interview_number())

        self.values.append(interview)

    def __len__(self) -> int:
        return len(self.values)

    def __getitem__(self, index: int) -> InterviewV3:
        return self.values[index]

    def next_interview_number(self) -> int:
        return len(self.values) + 1
