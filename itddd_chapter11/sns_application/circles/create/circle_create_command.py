from dataclasses import dataclass


@dataclass
class CircleCreateCommand:
    """
    クライアントでは、このコマンドオブジェクトを使って、
        サークルを作成するユーザ(⇔サークルのオーナー)のID
        および
        サークル名前を指定します
    """
    user_id: str
    name: str
