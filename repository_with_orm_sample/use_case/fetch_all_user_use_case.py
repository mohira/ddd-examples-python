from dataclasses import dataclass
from typing import List

from repository_with_orm_sample.domain.user_repository import UserRepository
from repository_with_orm_sample.use_case.user_dto import UserDto


@dataclass
class FetchAllUserUseCase:
    # MEMO: 薄すぎて気になっちゃうけど、別に困ることはないんだよね
    user_repository: UserRepository

    def fetch_all_users(self) -> List[UserDto]:
        domain_users = self.user_repository.find_all()

        # ドメインオブジェクトからDTOへの詰め替え
        return [UserDto.from_domain_user(user) for user in domain_users]
