import unittest

from task_management.src.domain.user.user_id import UserStatus
from task_management.src.domain_service.user.user_domain_service import UserDomainService
from task_management.src.infra.user.in_memory_user_repository import InMemoryUserRepository
from task_management.src.usecase.user.user_create_usecase import UserCreateUseCase
from task_management.src.usecase.user.user_deactivate_usecase import UserDeactivateUseCase


class TestUserDeactivateUseCase(unittest.TestCase):

    def test_ユーザーを非活性化できる(self):
        user_repository = InMemoryUserRepository()
        user_domain_service = UserDomainService(user_repository)

        user_id = UserCreateUseCase(user_repository, user_domain_service).create_user('Bob', 'bob@example.com')

        deactivate_usecase = UserDeactivateUseCase(user_repository)
        deactivate_usecase.deactivate(user_id)

        actual_user = user_repository.find_by_id(user_id)

        self.assertEqual(UserStatus.IN_ACTIVE, actual_user.user_status)


if __name__ == '__main__':
    unittest.main()
