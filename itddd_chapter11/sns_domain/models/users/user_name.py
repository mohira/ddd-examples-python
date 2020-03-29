from dataclasses import dataclass


@dataclass(frozen=True)
class UserName:
    value: str

    def __post_init__(self):
        if self.value is None:
            raise TypeError(self.value)

        if len(self.value) < 3:
            raise ValueError(f'サークル名は3文字以上です。 {self.value}')

        if len(self.value) > 20:
            raise ValueError(f'サークル名は20文字以下です。 {self.value}')
