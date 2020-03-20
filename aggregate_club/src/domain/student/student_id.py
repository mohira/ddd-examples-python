import uuid
from dataclasses import dataclass


@dataclass
class StudentId:
    value: str = str(uuid.uuid4())
