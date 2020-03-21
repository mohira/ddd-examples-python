from dataclasses import dataclass

from task_management.src.domain.user.user import User
from task_management.src.domain.user.user_id import UserId
from task_management.src.domain.user.user_repository import UserRepository


@dataclass
class UserCreateUseCase:
    user_repository: UserRepository

    def create_user(self, name: str, mail_address: str) -> UserId:
        user = User(name, mail_address)

        self.user_repository.save(user)

        return user.user_id
