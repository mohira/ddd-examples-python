from dataclasses import dataclass


@dataclass(frozen=True)
class CircleId:
    value: str

    def __post_init__(self):
        # post_initの方がわかりやすいと思っている
        if self.value is None:
            raise TypeError

        if self.value == '':
            raise ValueError
