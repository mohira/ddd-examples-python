import uuid
from dataclasses import dataclass


@dataclass(frozen=True)
class StudentId:
    value: str

    def __init__(self):
        object.__setattr__(self, 'value', str(uuid.uuid4()))

    def __str__(self):
        return self.value
