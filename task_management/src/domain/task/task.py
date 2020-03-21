import datetime
from dataclasses import dataclass, field

from task_management.src.domain.domain_exception import DomainException
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

    def postpone(self) -> None:
        self.validate_postpone_count()

        object.__setattr__(self, 'due_date', self.due_date + datetime.timedelta(days=1))
        object.__setattr__(self, 'postpone_count', self.postpone_count + 1)

    def validate_postpone_count(self) -> None:
        MAX_POSTPONE_COUNT = 3

        if self.postpone_count >= MAX_POSTPONE_COUNT:
            raise DomainException('タスクは3回までしか延期できません')
