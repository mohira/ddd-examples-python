import datetime
from dataclasses import dataclass

from task_management.src.domain.task.task import Task
from task_management.src.domain.task.task_id import TaskId
from task_management.src.domain.task.task_repository import TaskRepository


@dataclass
class TaskCreateUseCase:
    task_repository: TaskRepository

    def create_task(self, name: str, due_date: datetime.date) -> TaskId:
        task = Task(name, due_date)

        self.task_repository.save(task)

        return task.task_id
