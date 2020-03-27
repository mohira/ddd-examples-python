from enum import Enum


class ScreeningStepResult(Enum):
    NotEvaluated = '未評価'
    Pass = '合格'
    Fail = '不合格'
