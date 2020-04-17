from dataclasses import dataclass

from repository_with_orm_sample.use_case.domain_exceptions import CanNotRegisterUserNameException


@dataclass(frozen=True)
class UserName:
    value: str

    def __post_init__(self):
        # ドメイン知識を表現
        if len(self.value) <= 2:
            raise CanNotRegisterUserNameException('2文字以下のユーザ名は使用できません')

        if len(self.value) >= 21:
            raise CanNotRegisterUserNameException('21文字以上のユーザ名は使用できません')
