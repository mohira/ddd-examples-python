from __future__ import annotations

import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True)
class UserId:
    value: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'value', str(uuid.uuid4()))

    @classmethod
    def reconstruct(cls, value: str) -> UserId:
        """リポジトリ用の再構成メソッド"""
        user_id = UserId()

        object.__setattr__(user_id, 'value', value)

        return user_id
