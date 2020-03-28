from dataclasses import dataclass, asdict

from repository_with_orm_sample.domain.user_age import UserAge
from repository_with_orm_sample.domain.user_id import UserId
from repository_with_orm_sample.domain.user_name import UserName


@dataclass
class DomainUser:
    """ドメインオブジェクトとしてのUserクラス

    ドメインオブジェクトであることを忘れないために、わざと Domain という接頭辞をつけている
    """
    user_id: UserId
    user_name: UserName
    user_age: UserAge

    def as_csv(self) -> str:
        return ','.join([str(x['value']) for x in asdict(self).values()])
