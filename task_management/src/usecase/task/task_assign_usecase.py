from dataclasses import dataclass

from task_management.src.domain.task.task_id import TaskId
from task_management.src.domain.task.task_repository import TaskRepository
from task_management.src.domain.user.user_id import UserId


@dataclass
class TaskAssignUseCase:
    task_repository: TaskRepository

    def assign(self, task_id: TaskId, user_id: UserId) -> None:
        task = self.task_repository.find_by_id(task_id)

        task.assign(user_id)

        self.task_repository.save(task)
