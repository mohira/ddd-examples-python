from dataclasses import dataclass

from task_management.src.domain.task.task_id import TaskId
from task_management.src.domain.task.task_repository import TaskRepository


@dataclass
class TaskDoneUseCase:
    task_repository: TaskRepository

    def done_task(self, task_id: TaskId) -> None:
        task = self.task_repository.find_by_id(task_id)

        task.done()

        self.task_repository.save(task)
