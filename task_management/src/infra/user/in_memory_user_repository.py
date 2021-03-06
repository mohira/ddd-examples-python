from copy import deepcopy
from typing import Dict

from task_management.src.domain.user.user import User
from task_management.src.domain.user.user_id import UserId
from task_management.src.domain.user.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self):
        self.data_dict: Dict[UserId, User] = dict()

    def save(self, user: User) -> None:
        self.data_dict[user.user_id] = user

    def find_by_id(self, user_id: UserId) -> User:
        return deepcopy(self.data_dict[user_id])

    def find_by_mail_address(self, mail_address: str) -> User:
        for user_id, user in self.data_dict.items():
            if user.mail_address == mail_address:
                return deepcopy(self.data_dict[user_id])
