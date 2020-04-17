from dataclasses import dataclass

from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_age import UserAge
from repository_with_orm_sample.domain.user_id import UserId
from repository_with_orm_sample.domain.user_name import UserName
from repository_with_orm_sample.domain.user_repository import UserRepository
from repository_with_orm_sample.domain_service.user_domain_service import UserDomainService
from repository_with_orm_sample.use_case.domain_exceptions import CanNotRegisterDuplicatedUserException


@dataclass
class RegisterUserUseCae:
    user_repository: UserRepository
    user_domain_service: UserDomainService

    def create_user(self, name: str, age: int) -> UserId:
        domain_user = DomainUser(user_id=UserId(),
                                 user_name=UserName(name),
                                 user_age=UserAge(age))

        if self.user_domain_service.exists(domain_user):
            raise CanNotRegisterDuplicatedUserException(f'{name} は既に使用されているので登録できないのです')

        self.user_repository.register(domain_user)

        return domain_user.user_id
