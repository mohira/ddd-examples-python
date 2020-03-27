import datetime
from dataclasses import dataclass

from taiken_ddd.src.v2.domain.screening_repository import ScreeningRepository
from taiken_ddd.src.v2.domain.screening_v2 import ScreeningV2


@dataclass
class ScreeningApplicationServiceV2:
    screening_repository: ScreeningRepository

    def start_from_pre_interview(self, applicant_email_address: str) -> None:
        """面談から新規候補者を登録する"""
        screening = ScreeningV2.start_from_pre_interview(applicant_email_address)

        self.screening_repository.insert(screening)

    def apply(self, applicant_email_address: str) -> None:
        """新規応募者を登録する"""
        screening = ScreeningV2.apply(applicant_email_address)

        self.screening_repository.insert(screening)

    def add_next_interview(self, screening_id: str, interview_date: datetime.date) -> None:
        """次の面接を設定する"""
        screening = self.screening_repository.find_by_id(screening_id)

        screening.add_next_interview(interview_date)

        self.screening_repository.update(screening)

    # 面談から面接に進む処理は省略
