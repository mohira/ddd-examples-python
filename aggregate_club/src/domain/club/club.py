from dataclasses import dataclass, field
from typing import List

from aggregate_club.src.domain.club.club_id import ClubId
from aggregate_club.src.domain.club.club_status import ClubStatus
from aggregate_club.src.domain.domain_exception import DomainException
from aggregate_club.src.domain.student.student_id import StudentId

MINIMUM_APPROVAL_CONDITION = 5


@dataclass(frozen=True)
class Club:
    club_id: ClubId
    name: str
    club_status: ClubStatus = ClubStatus.NOT_APPROVED
    student_ids: List[StudentId] = field(default_factory=list)

    def add_student(self, student_id: StudentId) -> None:
        if student_id in self.student_ids:
            raise DomainException('既に登録済みの生徒です')

        self.student_ids.append(student_id)

    def approve(self) -> None:
        if len(self.student_ids) < MINIMUM_APPROVAL_CONDITION:
            raise DomainException('生徒数が5名未満なので承認できません。')

        object.__setattr__(self, 'club_status', ClubStatus.APPROVED)