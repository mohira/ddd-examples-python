import datetime
import unittest

from task_management.src.domain.user.user_id import UserId
from task_management.src.infra.task.in_memory_task_repository import InMemoryTaskRepository
from task_management.src.usecase.task.task_assign_usecase import TaskAssignUseCase
from task_management.src.usecase.task.task_create_usecase import TaskCreateUseCase


class TestTaskAssignUseCase(unittest.TestCase):
    def setUp(self) -> None:
        self.task_repository = InMemoryTaskRepository()
        self.task_id = TaskCreateUseCase(self.task_repository).create_task('タスクその1', datetime.date(2020, 4, 1))
        self.usecase = TaskAssignUseCase(self.task_repository)

    def test_タスクに担当者を設定できる(self):
        user_id = UserId()
        self.usecase.assign(self.task_id, user_id)

        actual_task = self.task_repository.find_by_id(self.task_id)

        self.assertEqual(user_id, actual_task.user_id)

    def test_タスクの担当者は上書きで変更される(self):
        old_assignee_id = UserId()
        self.usecase.assign(self.task_id, old_assignee_id)

        new_assignee_id = UserId()
        self.usecase.assign(self.task_id, new_assignee_id)

        actual_task = self.task_repository.find_by_id(self.task_id)

        self.assertEqual(new_assignee_id, actual_task.user_id)


if __name__ == '__main__':
    unittest.main()
