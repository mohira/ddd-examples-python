from dataclasses import dataclass

from aggregate_club.src.domain.club.club_id import ClubId
from aggregate_club.src.domain.club.club_repository import ClubRepository
from aggregate_club.src.domain.student.student_id import StudentId


@dataclass
class ClubUseCase:
    club_repository: ClubRepository

    def add_student(self, club_id: ClubId, student_id: StudentId):
        """クラブに生徒を登録します"""
        club = self.club_repository.find_by_id(club_id)
        club.add_student(student_id)
        self.club_repository.save(club)
