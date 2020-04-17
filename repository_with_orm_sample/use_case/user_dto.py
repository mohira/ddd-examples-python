from __future__ import annotations

from dataclasses import dataclass

from repository_with_orm_sample.domain.domain_user import DomainUser


@dataclass
class UserDto:
    id: str
    name: str
    age: int

    @staticmethod
    def from_domain_user(domain_user: DomainUser) -> UserDto:
        return UserDto(domain_user.user_id.value,
                       domain_user.user_name.value,
                       domain_user.user_age.value)
