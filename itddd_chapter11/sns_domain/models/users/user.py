from dataclasses import dataclass

from itddd_chapter11.sns_domain.models.users.user_id import UserId
from itddd_chapter11.sns_domain.models.users.user_name import UserName


@dataclass
class User:
    id: UserId
    name: UserName
