from abc import ABCMeta, abstractmethod
from typing import List, Optional

from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_id import UserId


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def register(self, user: DomainUser) -> None:
        pass

    @abstractmethod
    def find_all(self) -> List[DomainUser]:
        pass

    @abstractmethod
    def find_by_id(self, user_id: UserId) -> Optional[DomainUser]:
        pass

    @abstractmethod
    def find_by_name(self, name: str) -> Optional[DomainUser]:
        pass
