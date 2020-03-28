from __future__ import annotations

import datetime
import uuid
from dataclasses import dataclass, field
from typing import List

from taiken_ddd.src.shared.application_exception import ApplicationException
from taiken_ddd.src.v3.domain.interview_v3 import InterviewV3
from taiken_ddd.src.v3.domain.screening_status_v3 import ScreeningStatusV3


@dataclass(frozen=True)
class ScreeningV3:
    """採用選考クラス(面接でも、面談でもないよ)"""
    # ⑤ デフォルトコンストラクタをPrivateにしている雰囲気
    # Javaのように「インスタンス生成を不可能にする」は実現できないが、
    # それなりに "堅い" 感じになっているのでイメージは理解できると思う
    # このクラスの `field(init=False)` の 異様な感じ を見ればファクトリメソッドを使ってメッセージはわりと届きそう
    screening_id: str = field(init=False)
    apply_date: datetime.date = field(init=False)
    status: ScreeningStatusV3 = field(init=False)
    applicant_email_address: str = field(init=False)

    # InterviewはScreeningの集約内なので、インスタンス参照(⇔子オブジェクトとしてインスタンス保持)
    # V1のときはApplicationServiceでSetしていた！
    interviews: List[InterviewV3] = field(init=False)

    @classmethod
    def start_from_pre_interview(cls, applicant_email_address: str) -> ScreeningV3:
        """面談から採用選考を登録する際のファクトリメソッド"""
        # 不正なインスタンスを生成させないために、コンストラクタでチェックする
        if cls.__is_empty(applicant_email_address) or (cls.__is_invalid_format_email_address(applicant_email_address)):
            raise ApplicationException('メールアドレスが正しくありません')

        screening = ScreeningV3()

        object.__setattr__(screening, 'screening_id', str(uuid.uuid4()))
        object.__setattr__(screening, 'status', ScreeningStatusV3.NotApplied)  # ① 面談からの場合はステータス「未応募」で登録
        object.__setattr__(screening, 'apply_date', None)  # ② 未応募なので応募日はブランク
        object.__setattr__(screening, 'applicant_email_address', applicant_email_address)
        object.__setattr__(screening, 'interviews', [])

        return screening

    @classmethod
    def apply(cls, applicant_email_address: str) -> ScreeningV3:
        """面接から採用選考を登録する際のファクトリメソッド"""

        # 不正なインスタンスを生成させないために、コンストラクタでチェックする
        if cls.__is_empty(applicant_email_address) or (cls.__is_invalid_format_email_address(applicant_email_address)):
            raise ApplicationException('メールアドレスが正しくありません')

        screening = ScreeningV3()

        object.__setattr__(screening, 'screening_id', str(uuid.uuid4()))
        object.__setattr__(screening, 'status', ScreeningStatusV3.Interview)  # ③ 面接なので初期ステータス「選考中」で登録
        object.__setattr__(screening, 'apply_date', datetime.date.today())  # ④ 面接なので応募日は登録日
        object.__setattr__(screening, 'applicant_email_address', applicant_email_address)
        object.__setattr__(screening, 'interviews', [])

        return screening

    @classmethod
    def __is_empty(cls, applicant_email_address: str) -> bool:
        """文字列の空白チェック用メソッド"""
        return applicant_email_address == ''

    @classmethod
    def __is_invalid_format_email_address(cls, applicant_email_address: str) -> bool:
        """メールアドレスのバリデーション用メソッド"""
        # 適切なバリデーションが行われているとする
        return False

    def add_next_interview(self, interview_date: datetime.date) -> None:
        """ミューテーションメソッド"""

        # ① 選考ステータスが「選考中」以外のときには設定できない
        if self.status != ScreeningStatusV3.Interview:
            raise ApplicationException('不正な操作です。選考中でないときに次の面接を設定することはできません')

        # ② 面接次数は1からインクリメントされる
        next_interview_number = len(self.interviews) + 1
        next_interview = InterviewV3(interview_date, next_interview_number)

        self.interviews.append(next_interview)
