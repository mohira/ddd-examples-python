from dataclasses import dataclass
from typing import List

from itddd_chapter11.sns_domain.models.circles.circle_id import CircleId
from itddd_chapter11.sns_domain.models.circles.circle_name import CircleName
from itddd_chapter11.sns_domain.models.users.user import User


@dataclass(frozen=True)
class Circle:
    id: CircleId
    name: CircleName
    owner: User
    members: List[User]

    def __post_init__(self):
        if self.id is None:
            raise TypeError(self.id)

        if self.name is None:
            raise TypeError(self.name)

        if self.owner is None:
            raise TypeError(self.owner)

        if self.members is None:
            raise TypeError(self.members)
