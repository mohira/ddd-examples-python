import datetime
import uuid
from dataclasses import dataclass

from taiken_ddd.src.v1.domain.dao.interview_dao import InterviewDao
from taiken_ddd.src.v1.domain.dao.screening_dao import ScreeningDao
from taiken_ddd.src.v1.domain.screening_status_v1 import ScreeningStatusV1
from taiken_ddd.src.v1.domain.screening_v1 import ScreeningV1


@dataclass
class EvilScreeningApplicationServiceV1:
    """V1の実装だと、間違った実装が容易に作れてしまうという実例"""
    _screening_dao: ScreeningDao
    _interview_dao: InterviewDao

    def evil_start_from_pre_interview(self, applicant_email_address: str) -> None:
        """面談から新規候補者を登録するが、ルールや成約にことごとく違反する"""
        screening = ScreeningV1()

        # × IDは現在時刻をStringにしたもの → 時刻が被ったら死亡
        # https://docs.python.org/ja/3/library/uuid.html#uuid.uuid1
        screening.screening_id = str(uuid.uuid1())

        # x いきなり不合格で登録
        screening.status = ScreeningStatusV1.Refected

        # x 応募日をなぜか7日前に指定
        screening.apply_date = datetime.date.today() - datetime.timedelta(days=7)

        # x メールアドレスはバリデーションなしで引数の値をそのまま保存
        screening.applicant_email_address = applicant_email_address

        self._screening_dao.insert(screening)
