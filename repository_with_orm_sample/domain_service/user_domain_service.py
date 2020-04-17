from dataclasses import dataclass

from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_repository import UserRepository


@dataclass
class UserDomainService:
    user_repository: UserRepository

    def exists(self, user: DomainUser) -> bool:
        """ユーザ名の重複チェック"""
        duplicated_user = self.user_repository.find_by_name(user.user_name.value)

        return duplicated_user is not None
