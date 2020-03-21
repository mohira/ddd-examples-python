from dataclasses import dataclass

from task_management.src.domain.user.user_id import UserId
from task_management.src.domain.user.user_repository import UserRepository


@dataclass
class UserDeactivateUseCase:
    user_repository: UserRepository

    def deactivate(self, user_id: UserId):
        user = self.user_repository.find_by_id(user_id)

        user.deactivate()

        self.user_repository.save(user)
