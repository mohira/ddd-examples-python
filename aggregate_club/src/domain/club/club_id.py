import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class ClubId:
    value: str = str(uuid.uuid4())
