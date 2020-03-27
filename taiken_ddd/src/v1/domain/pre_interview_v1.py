import datetime
from dataclasses import dataclass


@dataclass
class PreInterviewV1:
    """面談クラス(面接じゃないよでもないよ)"""
    interviewer_id: str
    pre_interview_date: datetime.date
