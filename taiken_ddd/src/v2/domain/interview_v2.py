import datetime
import uuid
from dataclasses import dataclass, field

from taiken_ddd.src.v2.domain.screening_step_result import ScreeningStepResult


@dataclass(frozen=True)
class InterviewV2:
    """面接クラス(採用選考でも、面談でもないよ)"""
    interview_id: str = field(init=False)
    interview_date: datetime.date
    interview_number: int
    screening_step_result: ScreeningStepResult = field(default=None)

    # TODO: PR: `recruiter_id` が消えた？ 理由は「主題」出ないからだと思う(たぶん)

    def __post_init__(self):
        object.__setattr__(self, 'interview_id', str(uuid.uuid4()))
        object.__setattr__(self, 'screening_step_result', ScreeningStepResult.NotEvaluated)
