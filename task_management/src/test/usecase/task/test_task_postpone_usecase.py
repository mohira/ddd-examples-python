import datetime
import unittest

from task_management.src.domain.domain_exception import DomainException
from task_management.src.infra.task.in_memory_task_repository import InMemoryTaskRepository
from task_management.src.usecase.task.task_create_usecase import TaskCreateUseCase
from task_management.src.usecase.task.task_postpone_usecase import TaskPostponeUseCase


class TestTaskPostponeUseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.task_repository = InMemoryTaskRepository()
        self.task_id = TaskCreateUseCase(self.task_repository).create_task('タスクその1', datetime.date(2020, 4, 1))
        self.usecase = TaskPostponeUseCase(self.task_repository)

    def test_最大延期回数を下回っていればタスクを1日だけ延期できる(self):
        self.usecase.postpone_task(self.task_id)

        actual_task = self.task_repository.find_by_id(self.task_id)

        self.assertEqual(datetime.date(2020, 4, 2), actual_task.due_date)
        self.assertEqual(1, actual_task.postpone_count)

    def test_同一タスクの延期は3回までしかできない(self):
        for _ in range(3):
            self.usecase.postpone_task(self.task_id)

        with self.assertRaises(DomainException):
            self.usecase.postpone_task(self.task_id)


if __name__ == '__main__':
    unittest.main()
