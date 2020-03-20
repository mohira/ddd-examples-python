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

    def approve_club(self, club_id: ClubId) -> None:
        """条件を満たせば、クラブを承認します"""
        club = self.club_repository.find_by_id(club_id)
        club.approve()
        self.club_repository.save(club)

    def quit_student(self, club_id: ClubId, student_id: StudentId) -> None:
        """生徒を退部させます"""
        club = self.club_repository.find_by_id(club_id)

        club.quit(student_id)

        self.club_repository.save(club)
