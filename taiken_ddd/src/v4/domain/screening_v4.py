from __future__ import annotations

import datetime
from dataclasses import dataclass, field

from taiken_ddd.src.shared.application_exception import ApplicationException
from taiken_ddd.src.v3.domain.email_address import EmailAddress
from taiken_ddd.src.v3.domain.interviews import Interviews
from taiken_ddd.src.v3.domain.screening_id import ScreeningId
from taiken_ddd.src.v4.domain.screening_status_v4 import ScreeningStatusV4


@dataclass(frozen=True)
class ScreeningV4:
    """採用選考クラス(面接でも、面談でもないよ)"""
    screening_id: str = field(init=False)
    apply_date: datetime.date = field(init=False)
    status: ScreeningStatusV4 = field(init=False)
    applicant_email_address: str = field(init=False)
    interviews: Interviews = field(init=False)

    @classmethod
    def start_from_pre_interview(cls, applicant_email_address: str) -> ScreeningV4:
        """面談から採用選考を登録する際のファクトリメソッド"""
        screening = ScreeningV4()

        # EmailAddressインスタンスの生成は正しいものだけしか生成されないので、
        # Screeningクラスでのバリデーションは不要！
        object.__setattr__(screening, 'applicant_email_address', EmailAddress(applicant_email_address))

        object.__setattr__(screening, 'screening_id', ScreeningId())
        object.__setattr__(screening, 'status', ScreeningStatusV4.NotApplied)
        object.__setattr__(screening, 'apply_date', None)
        object.__setattr__(screening, 'interviews', Interviews())

        return screening

    @classmethod
    def apply(cls, applicant_email_address: str) -> ScreeningV4:
        """面接から採用選考を登録する際のファクトリメソッド"""
        screening = ScreeningV4()

        object.__setattr__(screening, 'applicant_email_address', EmailAddress(applicant_email_address))

        object.__setattr__(screening, 'screening_id', ScreeningId())
        object.__setattr__(screening, 'status', ScreeningStatusV4.Interview)
        object.__setattr__(screening, 'apply_date', datetime.date.today())
        object.__setattr__(screening, 'interviews', Interviews())

        return screening

    def add_next_interview(self, interview_date: datetime.date) -> None:
        """ミューテーションメソッド"""
        # どのステータスだとinterviewを追加できるかの判断は、ScreeningStatusに委譲
        if not self.status.can_add_interview():
            raise ApplicationException('不正な操作です。ステータスを確認してください。')

        self.interviews.add_next_interview(interview_date)
