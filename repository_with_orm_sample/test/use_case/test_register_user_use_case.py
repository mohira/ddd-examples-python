import unittest

from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_age import UserAge
from repository_with_orm_sample.domain.user_id import UserId
from repository_with_orm_sample.domain.user_name import UserName
from repository_with_orm_sample.domain_service.user_domain_service import UserDomainService
from repository_with_orm_sample.infra.in_memory_user_repository import InMemoryUserRepository
from repository_with_orm_sample.use_case.domain_exceptions import CanNotRegisterDuplicatedUserException, \
    CanNotRegisterNot20sUserException, CanNotRegisterUserNameException
from repository_with_orm_sample.use_case.register_user_use_case import RegisterUserUseCae


class TestUserCreateUseCase(unittest.TestCase):
    def setUp(self):
        self.user_repository = InMemoryUserRepository({})
        user_domain_service = UserDomainService(self.user_repository)
        self.use_case = RegisterUserUseCae(self.user_repository, user_domain_service)

    def test_新規ユーザを登録できる(self):
        user_id = self.use_case.create_user(name='Bob', age=25)

        expected_user = DomainUser(user_id, UserName('Bob'), UserAge(25))

        self.assertEqual(expected_user, self.user_repository.find_by_id(user_id))

    def test_同名のユーザは登録できない(self):
        registered_user = DomainUser(UserId(), UserName('Bob'), UserAge(25))
        self.user_repository.data_dict[registered_user.user_id] = registered_user

        with self.assertRaises(CanNotRegisterDuplicatedUserException):
            self.use_case.create_user(name='Bob', age=25)

    def test_2文字以下のユーザ名では登録できない(self):
        with self.assertRaises(CanNotRegisterUserNameException):
            self.use_case.create_user(name='B', age=25)

    def test_20代のユーザしか登録できない(self):
        with self.assertRaises(CanNotRegisterNot20sUserException):
            self.use_case.create_user(name='Bob', age=34)


if __name__ == '__main__':
    unittest.main()
