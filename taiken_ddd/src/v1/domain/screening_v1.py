import datetime
from dataclasses import dataclass, field

from taiken_ddd.src.v1.domain.screening_status_v1 import ScreeningStatusV1


@dataclass
class ScreeningV1:
    """採用選考クラス(面接でも、面談でもないよ)"""
    screening_id: str = field(default=None)
    apply_date: datetime.date = field(default=None)
    status: ScreeningStatusV1 = field(default=None)
    applicant_email_address: str = field(default=None)
