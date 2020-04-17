from dataclasses import dataclass
from typing import List

from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_repository import UserRepository


@dataclass
class FetchAllUserUseCase:
    # MEMO: 薄すぎて気になっちゃうけど、別に困ることはないんだよね
    user_repository: UserRepository

    def fetch_all_users(self) -> List[DomainUser]:
        return self.user_repository.find_all()
