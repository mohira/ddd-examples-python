from __future__ import annotations

import uuid
from dataclasses import dataclass, field
from enum import Enum


@dataclass(frozen=True)
class UserId:
    value: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'value', str(uuid.uuid4()))


class UserStatus(Enum):
    ACTIVE = '活性化'
    NOT_ACTIVE = '非活性化'
