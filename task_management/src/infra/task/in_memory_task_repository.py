from copy import deepcopy
from typing import Dict

from task_management.src.domain.task.task import Task
from task_management.src.domain.task.task_id import TaskId
from task_management.src.domain.task.task_repository import TaskRepository


class InMemoryTaskRepository(TaskRepository):
    def __init__(self):
        self.data_dict: Dict[TaskId, Task] = dict()

    def save(self, task: Task) -> None:
        self.data_dict[task.task_id] = task

    def find_by_id(self, task_id: TaskId) -> Task:
        return deepcopy(self.data_dict[task_id])
