from dataclasses import dataclass


@dataclass(frozen=True)
class UserName:
    value: str

    def __post_init__(self):
        # ドメイン知識を表現
        if len(self.value) <= 2:
            raise ValueError('2文字以下のユーザ名は使用できません')

        if len(self.value) >= 21:
            raise ValueError('21文字以上のユーザ名は使用できません')
