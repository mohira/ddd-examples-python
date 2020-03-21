import datetime
from dataclasses import dataclass, field

from task_management.src.domain.domain_exception import DomainException
from task_management.src.domain.task.task_id import TaskId
from task_management.src.domain.task.task_status import TaskStatus
from task_management.src.domain.user.user_id import UserId


@dataclass(frozen=True)
class Task:
    task_id: TaskId = field(init=False)
    name: str
    due_date: datetime.date
    task_status: TaskStatus = field(init=False)
    postpone_count: int = field(init=False)

    user_id: UserId = field(init=False)

    def __post_init__(self):
        object.__setattr__(self, 'task_id', TaskId())
        object.__setattr__(self, 'task_status', TaskStatus.UNDONE)
        object.__setattr__(self, 'postpone_count', 0)

        object.__setattr__(self, 'user_id', None)

    def postpone(self) -> None:
        self.validate_postpone_count()

        object.__setattr__(self, 'due_date', self.due_date + datetime.timedelta(days=1))
        object.__setattr__(self, 'postpone_count', self.postpone_count + 1)

    def validate_postpone_count(self) -> None:
        MAX_POSTPONE_COUNT = 3

        if self.postpone_count >= MAX_POSTPONE_COUNT:
            raise DomainException('タスクは3回までしか延期できません')

    def done(self) -> None:
        if self.task_status == TaskStatus.DONE:
            raise DomainException('既に完了しています')

        object.__setattr__(self, 'task_status', TaskStatus.DONE)

    def assign(self, user_id: UserId) -> None:
        object.__setattr__(self, 'user_id', user_id)
