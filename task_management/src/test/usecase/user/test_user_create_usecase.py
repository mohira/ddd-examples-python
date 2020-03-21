import unittest

from task_management.src.domain.user.user_id import UserStatus
from task_management.src.infra.user.in_memory_user_repository import InMemoryUserRepository
from task_management.src.usecase.user.user_create_usecase import UserCreateUseCase


class TestUserCreateUseCase(unittest.TestCase):
    def test_新規ユーザーを登録できる(self):
        user_repository = InMemoryUserRepository()

        usecase = UserCreateUseCase(user_repository)

        user_id = usecase.create_user(name='Bob', mail_address='bob@example.com')

        actual_user = user_repository.find_by_id(user_id)

        self.assertEqual('Bob', actual_user.name)
        self.assertEqual('bob@example.com', actual_user.mail_address)
        self.assertEqual(UserStatus.ACTIVE, actual_user.user_status)


if __name__ == '__main__':
    unittest.main()
