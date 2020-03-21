import datetime
from dataclasses import dataclass, field

from task_management.src.domain.task.task_id import TaskId
from task_management.src.domain.task.task_status import TaskStatus


@dataclass(frozen=True)
class Task:
    # MEMO: user_id は 不要なのか？
    task_id: TaskId = field(init=False)
    name: str
    due_date: datetime.date
    task_status: TaskStatus = field(init=False)
    postpone_count: int = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'task_id', TaskId())
        object.__setattr__(self, 'task_status', TaskStatus.UNDONE)
        object.__setattr__(self, 'postpone_count', 0)
