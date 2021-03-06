import uuid
from dataclasses import dataclass, field


@dataclass(frozen=True)
class TaskId:
    value: str = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'value', str(uuid.uuid4()))
