from dataclasses import dataclass, field

from task_management.src.domain.user.user_id import UserId, UserStatus


@dataclass(frozen=True)
class User:
    user_id: UserId = field(init=False)
    name: str
    mail_address: str  # MEMO: 全体的な実装を優先したいので、ひとまずstrにしておく(MailAddressクラスはあとでね)
    user_status: UserStatus = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'user_id', UserId())
        object.__setattr__(self, 'user_status', UserStatus.ACTIVE)
