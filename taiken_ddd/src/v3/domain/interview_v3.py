import datetime
import uuid
from dataclasses import dataclass, field

from taiken_ddd.src.v3.domain.screening_step_result import ScreeningStepResult


@dataclass(frozen=True)
class InterviewV3:
    """面接クラス(採用選考でも、面談でもないよ)"""
    interview_id: str = field(init=False)
    interview_date: datetime.date
    interview_number: int
    screening_step_result: ScreeningStepResult = field(default=None)

    def __post_init__(self):
        object.__setattr__(self, 'interview_id', str(uuid.uuid4()))
        object.__setattr__(self, 'screening_step_result', ScreeningStepResult.NotEvaluated)
