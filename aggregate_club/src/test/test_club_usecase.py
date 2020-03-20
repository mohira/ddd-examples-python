import unittest

from aggregate_club.src.domain.club.club import Club
from aggregate_club.src.domain.club.club_id import ClubId
from aggregate_club.src.domain.club.club_status import ClubStatus
from aggregate_club.src.domain.student.student_id import StudentId
from aggregate_club.src.infra.club.in_memory_club_repository import InMemoryClubRepository
from aggregate_club.src.usecase.club_usecase import ClubUseCase


class TestClubUseCase(unittest.TestCase):
    def test_add_student(self):
        club_id = ClubId()

        dummy_clubs = {club_id: Club(club_id=club_id, name='dummy_name')}

        club_repository = InMemoryClubRepository(dummy_clubs)

        club_usecase = ClubUseCase(club_repository)

        student_id = StudentId()

        club_usecase.add_student(club_id, student_id)

        expected = Club(club_id=club_id,
                        name='dummy_name',
                        club_status=ClubStatus.NOT_APPROVED,
                        student_ids=[student_id])

        self.assertEqual(expected, club_repository.data_dict[club_id])


if __name__ == '__main__':
    unittest.main()
