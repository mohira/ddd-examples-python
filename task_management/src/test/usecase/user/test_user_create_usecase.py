import unittest

from task_management.src.domain.domain_exception import DomainException
from task_management.src.domain.user.user_id import UserStatus
from task_management.src.domain_service.user.user_domain_service import UserDomainService
from task_management.src.infra.user.in_memory_user_repository import InMemoryUserRepository
from task_management.src.usecase.user.user_create_usecase import UserCreateUseCase


class TestUserCreateUseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.user_repository = InMemoryUserRepository()
        user_domain_service = UserDomainService(self.user_repository)
        self.usecase = UserCreateUseCase(self.user_repository, user_domain_service)

    def test_新規ユーザーを登録できる(self):
        user_id = self.usecase.create_user(name='Bob', mail_address='bob@example.com')

        actual_user = self.user_repository.find_by_id(user_id)

        self.assertEqual('Bob', actual_user.name)
        self.assertEqual('bob@example.com', actual_user.mail_address)
        self.assertEqual(UserStatus.ACTIVE, actual_user.user_status)

    def test_同一のメールアドレスでのユーザー登録はできない(self):
        # 実装の参考: https://github.com/nrslib/itddd/blob/a918365c24f199660b861e72b6ef1a3450a19129/SampleCodes/Chapter8/_13_to_17.Tests/Users/UserRegisterTest.cs
        self.usecase.create_user(name='Bob', mail_address='bob@example.com')

        with self.assertRaises(DomainException):
            self.usecase.create_user(name='Tom', mail_address='bob@example.com')


if __name__ == '__main__':
    unittest.main()
