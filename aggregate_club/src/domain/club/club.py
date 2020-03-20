from dataclasses import dataclass, field
from typing import List

from aggregate_club.src.domain.club.club_id import ClubId
from aggregate_club.src.domain.club.club_status import ClubStatus
from aggregate_club.src.domain.student.student_id import StudentId


@dataclass(frozen=True)
class Club:
    club_id: ClubId
    name: str
    club_status: ClubStatus = ClubStatus.NOT_APPROVED
    student_ids: List[StudentId] = field(default_factory=list)

    def add_student(self, student_id: StudentId) -> None:
        self.student_ids.append(student_id)
