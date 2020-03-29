from abc import ABCMeta, abstractmethod

from itddd_chapter11.sns_domain.models.users.user import User
from itddd_chapter11.sns_domain.models.users.user_id import UserId


class IUserRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_id(self, user_id: UserId) -> User:
        pass
