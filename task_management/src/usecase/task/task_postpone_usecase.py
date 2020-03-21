from dataclasses import dataclass

from task_management.src.domain.task.task_id import TaskId
from task_management.src.domain.task.task_repository import TaskRepository


@dataclass
class TaskPostponeUseCase:
    task_repository: TaskRepository

    def postpone_task(self, task_id: TaskId) -> None:
        task = self.task_repository.find_by_id(task_id)

        task.postpone()

        self.task_repository.save(task)
