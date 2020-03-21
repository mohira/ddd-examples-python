from dataclasses import dataclass

from task_management.src.domain.domain_exception import DomainException
from task_management.src.domain.user.user import User
from task_management.src.domain.user.user_id import UserId
from task_management.src.domain.user.user_repository import UserRepository
from task_management.src.domain_service.user.user_domain_service import UserDomainService


@dataclass
class UserCreateUseCase:
    user_repository: UserRepository
    user_domain_service: UserDomainService

    def create_user(self, name: str, mail_address: str) -> UserId:
        user = User(name, mail_address)

        if self.user_domain_service.exists(user):
            raise DomainException(f'{mail_address} は既に登録されています')

        self.user_repository.save(user)

        return user.user_id
