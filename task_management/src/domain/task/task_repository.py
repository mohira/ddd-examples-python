from abc import ABCMeta, abstractmethod

from task_management.src.domain.task.task import Task
from task_management.src.domain.task.task_id import TaskId


class TaskRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, task: Task) -> None:
        pass

    @abstractmethod
    def find_by_id(self, task_id: TaskId) -> Task:
        pass
