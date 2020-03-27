import datetime
from dataclasses import dataclass, field

from taiken_ddd.src.v2.domain.screening_step_result import ScreeningStepResult


@dataclass
class InterviewV2:
    """面接クラス(採用選考でも、面談でもないよ)"""
    interview_id: str = field(default=None)
    screening_id: str = field(default=None)
    screening_date: datetime.date = field(default=None)
    interview_number: int = field(default=None)
    screening_step_result: ScreeningStepResult = field(default=None)
    recruiter_id: int = field(default=None)
