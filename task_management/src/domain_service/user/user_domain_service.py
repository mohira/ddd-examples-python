from dataclasses import dataclass

from task_management.src.domain.user.user import User
from task_management.src.domain.user.user_repository import UserRepository


@dataclass
class UserDomainService:
    user_repository: UserRepository

    def exists(self, user: User) -> bool:
        user = self.user_repository.find_by_mail_address(user.mail_address)

        return user is not None
