import unittest

from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_age import UserAge
from repository_with_orm_sample.domain.user_id import UserId
from repository_with_orm_sample.domain.user_name import UserName
from repository_with_orm_sample.infra.in_memory_user_repository import InMemoryUserRepository
from repository_with_orm_sample.use_case.fetch_all_user_use_case import FetchAllUserUseCase


class TestFetchAllUserUseCase(unittest.TestCase):

    def test_新規ユーザを登録できる(self):
        user_repository = InMemoryUserRepository({})
        use_case = FetchAllUserUseCase(user_repository)

        bob = DomainUser(UserId(), UserName('Bob'), UserAge(25))
        tom = DomainUser(UserId(), UserName('Tom'), UserAge(26))
        ken = DomainUser(UserId(), UserName('Ken'), UserAge(27))

        user_repository.data_dict[bob.user_id] = bob
        user_repository.data_dict[tom.user_id] = tom
        user_repository.data_dict[ken.user_id] = ken

        self.assertEqual([bob, tom, ken], use_case.fetch_all_users())


if __name__ == '__main__':
    unittest.main()
