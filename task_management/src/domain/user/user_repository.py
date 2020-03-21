from abc import ABCMeta, abstractmethod

from task_management.src.domain.user.user import User
from task_management.src.domain.user.user_id import UserId


class UserRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, user: User) -> None:
        pass

    @abstractmethod
    def find_by_id(self, user_id: UserId) -> User:
        pass
