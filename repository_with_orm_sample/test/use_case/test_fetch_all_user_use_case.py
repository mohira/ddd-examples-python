import unittest

from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_age import UserAge
from repository_with_orm_sample.domain.user_id import UserId
from repository_with_orm_sample.domain.user_name import UserName
from repository_with_orm_sample.infra.in_memory_user_repository import InMemoryUserRepository
from repository_with_orm_sample.use_case.fetch_all_user_use_case import FetchAllUserUseCase
from repository_with_orm_sample.use_case.user_dto import UserDto


class TestFetchAllUserUseCase(unittest.TestCase):

    def test_ユーザ一覧を取得できる(self):
        user_repository = InMemoryUserRepository({})
        use_case = FetchAllUserUseCase(user_repository)

        bob = DomainUser(UserId(), UserName('Bob'), UserAge(25))
        tom = DomainUser(UserId(), UserName('Tom'), UserAge(26))
        ken = DomainUser(UserId(), UserName('Ken'), UserAge(27))

        user_repository.data_dict[bob.user_id] = bob
        user_repository.data_dict[tom.user_id] = tom
        user_repository.data_dict[ken.user_id] = ken

        expected = [UserDto(bob.user_id.value, bob.user_name.value, bob.user_age.value),
                    UserDto(tom.user_id.value, tom.user_name.value, tom.user_age.value),
                    UserDto(ken.user_id.value, ken.user_name.value, ken.user_age.value)]

        self.assertEqual(expected, use_case.fetch_all_users())


if __name__ == '__main__':
    unittest.main()
