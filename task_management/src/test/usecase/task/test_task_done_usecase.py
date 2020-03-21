import datetime
import unittest

from task_management.src.domain.domain_exception import DomainException
from task_management.src.domain.task.task_status import TaskStatus
from task_management.src.infra.task.in_memory_task_repository import InMemoryTaskRepository
from task_management.src.usecase.task.task_create_usecase import TaskCreateUseCase
from task_management.src.usecase.task.task_done_usecase import TaskDoneUseCase


class TestTaskDoneUseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.task_repository = InMemoryTaskRepository()
        self.task_id = TaskCreateUseCase(self.task_repository).create_task('タスクその1', datetime.date(2020, 4, 1))

        self.usecase = TaskDoneUseCase(self.task_repository)

    def test_未完了のタスクを完了にできる(self):
        self.usecase.done_task(self.task_id)

        actual_task = self.task_repository.find_by_id(self.task_id)

        self.assertEqual(TaskStatus.DONE, actual_task.task_status)

    def test_既に完了しているタスクへの完了処理はできない(self):
        self.usecase.done_task(self.task_id)

        with self.assertRaises(DomainException):
            self.usecase.done_task(self.task_id)


if __name__ == '__main__':
    unittest.main()
