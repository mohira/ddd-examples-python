from enum import Enum


class ScreeningStatusV3(Enum):
    NotApplied = '未応募'
    Interview = '面接選考中'
    Refected = '不合格'
    Passed = '合格'
