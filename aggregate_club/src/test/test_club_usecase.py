import unittest

from aggregate_club.src.domain.club.club import Club, MINIMUM_APPROVAL_CONDITION
from aggregate_club.src.domain.club.club_id import ClubId
from aggregate_club.src.domain.club.club_status import ClubStatus
from aggregate_club.src.domain.domain_exception import DomainException
from aggregate_club.src.domain.student.student_id import StudentId
from aggregate_club.src.infra.club.in_memory_club_repository import InMemoryClubRepository
from aggregate_club.src.usecase.club_usecase import ClubUseCase


class TestClubUseCase(unittest.TestCase):
    def test_add_student(self):
        with self.subTest('新しい部員を登録できる'):
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

        with self.subTest('既に所属している部員は新たに登録できない'):
            club_id = ClubId()

            student_id = StudentId()

            dummy_clubs = {club_id: Club(club_id=club_id, name='dummy_name', student_ids=[student_id])}

            club_repository = InMemoryClubRepository(dummy_clubs)

            club_usecase = ClubUseCase(club_repository)

            with self.assertRaises(DomainException):
                club_usecase.add_student(club_id, student_id)

    def test_approve_club(self):
        with self.subTest('5名以上の部員がいれば承認できる'):
            club_id = ClubId()

            student_ids_satisfied_approval_condition = [StudentId()] * MINIMUM_APPROVAL_CONDITION

            dummy_clubs = {club_id: Club(club_id=club_id, name='dummy_name',
                                         student_ids=student_ids_satisfied_approval_condition)}

            club_repository = InMemoryClubRepository(dummy_clubs)

            club_usecase = ClubUseCase(club_repository)

            club_usecase.approve_club(club_id)

            expected = Club(club_id=club_id, name='dummy_name',
                            club_status=ClubStatus.APPROVED,
                            student_ids=student_ids_satisfied_approval_condition)

            self.assertEqual(expected, club_repository.data_dict[club_id])

        with self.subTest('部員が5名未満の場合は承認できない'):
            club_id = ClubId()

            number_of_students = (MINIMUM_APPROVAL_CONDITION - 1)

            student_ids_not_satisfied_approval_condition = [StudentId()] * number_of_students

            dummy_clubs = {club_id: Club(club_id=club_id, name='dummy_name',
                                         student_ids=student_ids_not_satisfied_approval_condition)}

            club_repository = InMemoryClubRepository(dummy_clubs)

            club_usecase = ClubUseCase(club_repository)

            with self.assertRaises(DomainException):
                club_usecase.approve_club(club_id)


if __name__ == '__main__':
    unittest.main()
