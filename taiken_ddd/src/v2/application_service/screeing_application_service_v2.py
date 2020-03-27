import datetime
import uuid
from dataclasses import dataclass
from typing import List

from taiken_ddd.src.shared.application_exception import ApplicationException
from taiken_ddd.src.v1.domain.dao.interview_dao import InterviewDao
from taiken_ddd.src.v1.domain.dao.screening_dao import ScreeningDao
from taiken_ddd.src.v2.domain.interview_v2 import InterviewV2
from taiken_ddd.src.v2.domain.screening_status_v2 import ScreeningStatusV2
from taiken_ddd.src.v2.domain.screening_v2 import ScreeningV2


@dataclass
class ScreeningApplicationServiceV2:
    _screening_dao: ScreeningDao
    _interview_dao: InterviewDao

    def start_from_pre_interview(self, applicant_email_address: str) -> None:
        """面談から新規候補者を登録する"""

        # 入力のチェック
        if self.is_empty(applicant_email_address) or (self.is_invalid_format_email_address(applicant_email_address)):
            raise ApplicationException('メールアドレスが正しくありません')

        # デフォルトコンストラクタでインスタンス作成
        screening = ScreeningV2()
        screening.screening_id = str(uuid.uuid4())
        screening.status = ScreeningStatusV2.NotApplied  # 面談からの場合はステータス「未応募」で登録
        screening.apply_date = None  # 未応募なので応募日はNone
        screening.applicant_email_address = applicant_email_address

        self._screening_dao.insert(screening)

    def is_empty(self, applicant_email_address: str) -> bool:
        """文字列の空白チェック用メソッド"""
        return applicant_email_address == ''

    def is_invalid_format_email_address(self, applicant_email_address: str) -> bool:
        """メールアドレスのバリデーション用メソッド"""
        # 適切なバリデーションが行われているとする
        return False

    def apply(self, applicant_email_address: str) -> None:
        """新規応募者を登録する"""
        if self.is_empty(applicant_email_address) or self.is_invalid_format_email_address(applicant_email_address):
            raise ApplicationException('メールアドレスが正しくありません')

        screening = ScreeningV2()
        screening.screening_id = str(uuid.uuid4())
        screening.status = ScreeningStatusV2.Interview
        screening.apply_date = datetime.date.today()
        screening.applicant_email_address = applicant_email_address

        self._screening_dao.insert(screening)

    def add_next_interview(self, screening_id: str, interview_date: datetime.date) -> None:
        """次の面接を設定する"""

        # 保存されている採用選考オブジェクトを取得
        screening: ScreeningV2 = self._screening_dao.find_screening_by_id(screening_id)

        # 面接設定をしてよいステータスかをチェック
        if screening.status != ScreeningStatusV2.Interview:
            raise ApplicationException('選考ステータスが「選考中」以外のときには、面接は設定できません')

        # 保存されている面接オブジェクトの一覧を取得
        interviews: List[InterviewV2] = self._interview_dao.find_by_screening_id(screening_id)

        interview = InterviewV2()
        interview.interview_id = str(uuid.uuid4())
        interview.screening_id = screening_id
        interview.interview_number = len(interviews) + 1
        interview.screening_date = interview_date

        self._interview_dao.insert(interview)

    # 面談から面接に進む処理は省略
