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
        club_id = ClubId()

        student_id = StudentId()

        with self.subTest('新しい部員を登録できる'):
            club_repository = InMemoryClubRepository({club_id: Club(club_id=club_id, name='dummy_name')})

            club_usecase = ClubUseCase(club_repository)

            club_usecase.add_student(club_id, student_id)

            self.assertEqual(Club(club_id=club_id,
                                  name='dummy_name',
                                  club_status=ClubStatus.NOT_APPROVED,
                                  student_ids=[student_id]),
                             club_repository.data_dict[club_id])

        with self.subTest('既に所属している部員は新たに登録できない'):
            club_repository = InMemoryClubRepository({club_id: Club(club_id=club_id,
                                                                    name='dummy_name',
                                                                    student_ids=[student_id])})

            club_usecase = ClubUseCase(club_repository)

            with self.assertRaises(DomainException):
                club_usecase.add_student(club_id, student_id)

    def test_approve_club(self):
        club_id = ClubId()

        with self.subTest('承認条件を満たすだけの部員がいれば承認される'):
            student_ids_satisfied_approval_condition = [StudentId() for _ in range(MINIMUM_APPROVAL_CONDITION)]

            club_repository = InMemoryClubRepository({club_id: Club(club_id=club_id, name='dummy_name',
                                                                    student_ids=student_ids_satisfied_approval_condition)})

            club_usecase = ClubUseCase(club_repository)

            club_usecase.approve_club(club_id)

            self.assertEqual(Club(club_id=club_id, name='dummy_name',
                                  club_status=ClubStatus.APPROVED,
                                  student_ids=student_ids_satisfied_approval_condition),
                             club_repository.data_dict[club_id])

        with self.subTest('承認条件を下回る部員数の場合には承認されない'):
            student_ids_not_satisfied_approval_condition = [StudentId() for _ in range(MINIMUM_APPROVAL_CONDITION - 1)]

            club_repository = InMemoryClubRepository({club_id: Club(club_id=club_id, name='dummy_name',
                                                                    student_ids=student_ids_not_satisfied_approval_condition)})

            club_usecase = ClubUseCase(club_repository)

            with self.assertRaises(DomainException):
                club_usecase.approve_club(club_id)

    def test_quit_club(self):
        club_id = ClubId()
        quit_target_student_id = StudentId()

        with self.subTest('所属している生徒を退部させることができる'):
            club_repository = InMemoryClubRepository({club_id: Club(club_id=club_id,
                                                                    name='dummy_name',
                                                                    student_ids=[quit_target_student_id])})

            club_usecase = ClubUseCase(club_repository)

            club_usecase.quit_student(club_id, quit_target_student_id)

            self.assertEqual(Club(club_id=club_id, name='dummy_name', student_ids=[]),
                             club_repository.data_dict[club_id])

        with self.subTest('所属していない生徒は退部させることはできない'):
            club_repository = InMemoryClubRepository({club_id: Club(club_id=club_id,
                                                                    name='dummy_name',
                                                                    student_ids=[quit_target_student_id])})

            club_usecase = ClubUseCase(club_repository)

            other_student_id = StudentId()

            with self.assertRaises(DomainException):
                club_usecase.quit_student(club_id, other_student_id)

        with self.subTest('退部処理後に部員数が最低承認条件を下回った場合は未承認状態になる'):
            id_a, id_b, id_c, id_d = (StudentId() for _ in range(4))

            club_repository = InMemoryClubRepository({club_id: Club(club_id=club_id,
                                                                    name='dummy_name',
                                                                    club_status=ClubStatus.APPROVED,
                                                                    student_ids=[quit_target_student_id,
                                                                                 id_a, id_b, id_c, id_d])})

            club_usecase = ClubUseCase(club_repository)

            club_usecase.quit_student(club_id, quit_target_student_id)

            self.assertEqual(Club(club_id=club_id,
                                  name='dummy_name',
                                  club_status=ClubStatus.NOT_APPROVED,
                                  student_ids=[id_a, id_b, id_c, id_d]),
                             club_repository.data_dict[club_id])


if __name__ == '__main__':
    unittest.main()
