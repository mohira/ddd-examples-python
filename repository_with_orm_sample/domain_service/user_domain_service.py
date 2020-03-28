from dataclasses import dataclass

from repository_with_orm_sample.db_config import DB_CONFIG
from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_age import UserAge
from repository_with_orm_sample.domain.user_id import UserId
from repository_with_orm_sample.domain.user_name import UserName
from repository_with_orm_sample.domain.user_repository import UserRepository
from repository_with_orm_sample.infra.orator_user_repository import OratorUserRepository


@dataclass
class UserDomainService:
    user_repository: UserRepository

    def exists(self, user: DomainUser) -> bool:
        """ユーザ名の重複チェック"""
        duplicated_user = self.user_repository.find_by_name(user.user_name.value)

        return duplicated_user is not None


def main():
    user_repository = OratorUserRepository(DB_CONFIG)
    user_domain_service = UserDomainService(user_repository)

    print(user_domain_service.exists(user=DomainUser(UserId(), UserName('Bob'), UserAge(25))))

    print(user_domain_service.exists(user=DomainUser(UserId(), UserName('存在しないユーザ名'), UserAge(25))))


if __name__ == '__main__':
    main()
