from enum import Enum


class ScreeningStatusV4(Enum):
    NotApplied = False
    Interview = True
    Refected = False
    Passed = False

    def can_add_interview(self) -> bool:
        """面接可否を返す"""

        # JavaのEnumと違うのでそのまま value を返している
        # ただし、この場合、repr() では Falseの意味が汲み取れないと思う
        # can_add_interview() をみれば、さすがにわかると思うけど。
        # かといって、Enumの要素を変にdictにしてもちょっとアレだなあと思う

        return self.value
