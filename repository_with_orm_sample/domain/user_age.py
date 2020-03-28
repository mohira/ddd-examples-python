from dataclasses import dataclass


@dataclass(frozen=True)
class UserAge:
    value: int

    def __post_init__(self):
        # ドメイン知識を表現
        # やや無理があるけど「20代限定のサービス」というような設定ということで勘弁
        if not (20 <= self.value <= 29):
            raise ValueError('20代専用ですよ')
