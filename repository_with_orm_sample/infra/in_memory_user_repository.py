from dataclasses import dataclass
from typing import Dict, Optional, List

from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_id import UserId
from repository_with_orm_sample.domain.user_repository import UserRepository


@dataclass
class InMemoryUserRepository(UserRepository):
    data_dict: Dict[UserId, DomainUser]

    def register(self, user: DomainUser) -> None:
        self.data_dict[user.user_id] = user

    def find_by_id(self, user_id: UserId) -> Optional[DomainUser]:
        return self.data_dict[user_id]

    def find_by_name(self, name: str) -> Optional[DomainUser]:
        for user_id, user in self.data_dict.items():
            if user.user_name.value == name:
                return user

    def find_all(self) -> List[DomainUser]:
        return [user for user in self.data_dict.values()]
