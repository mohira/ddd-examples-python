from dataclasses import dataclass

import pytest

from repository_with_orm_sample.db_config import DB_CONFIG
from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_age import UserAge
from repository_with_orm_sample.domain.user_id import UserId
from repository_with_orm_sample.domain.user_name import UserName
from repository_with_orm_sample.domain.user_repository import UserRepository
from repository_with_orm_sample.domain_service.user_domain_service import UserDomainService
from repository_with_orm_sample.infra.orator_user_repository import OratorUserRepository
from repository_with_orm_sample.use_case.domain.domain_exceptions import CanNotRegisterUserException


@dataclass
class RegisterUserUseCae:
    user_repository: UserRepository
    user_domain_service: UserDomainService

    def create_user(self, name: str, age: int) -> None:
        domain_user = DomainUser(user_id=UserId(),
                                 user_name=UserName(name),
                                 user_age=UserAge(age))

        if self.user_domain_service.exists(domain_user):
            raise CanNotRegisterUserException(f'"{name}" は既に使用されているので登録できないのです')

        self.user_repository.register(domain_user)


def main():
    user_repository = OratorUserRepository(DB_CONFIG)
    user_domain_service = UserDomainService(user_repository)
    use_case = RegisterUserUseCae(user_repository, user_domain_service)

    with pytest.raises(ValueError):
        use_case.create_user(name='a', age=25)

    with pytest.raises(ValueError):
        use_case.create_user(name='Bob', age=35)

    use_case.create_user(name='Ken', age=20)
    use_case.create_user(name='Bob', age=25)
    use_case.create_user(name='Tom', age=28)


if __name__ == '__main__':
    main()
