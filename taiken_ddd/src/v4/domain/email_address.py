from __future__ import annotations

from dataclasses import dataclass

from taiken_ddd.src.shared.application_exception import ApplicationException


@dataclass
class EmailAddress:
    value: str

    def __post_init__(self):
        if self.is_empty(self.value) or self.is_invalid_format_email_address(self.value):
            raise ApplicationException('メールアドレスが正しくありません')

    def is_empty(self, applicant_email_address: str) -> bool:
        """文字列の空白チェック用メソッド"""
        return applicant_email_address == ''

    def is_invalid_format_email_address(self, applicant_email_address: str) -> bool:
        """メールアドレスのバリデーション用メソッド"""
        # 適切なバリデーションが行われているとする
        return False
