from __future__ import annotations

import datetime
from dataclasses import dataclass, field

from taiken_ddd.src.v2.domain.screening_status_v2 import ScreeningStatusV2


@dataclass
class ScreeningV2:
    """採用選考クラス(面接でも、面談でもないよ)"""
    screening_id: str = field(default=None)
    apply_date: datetime.date = field(default=None)
    status: ScreeningStatusV2 = field(default=None)
    applicant_email_address: str = field(default=None)

