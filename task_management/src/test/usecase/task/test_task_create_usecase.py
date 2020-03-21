import datetime
import unittest

from task_management.src.domain.task.task_status import TaskStatus
from task_management.src.infra.task.in_memory_task_repository import InMemoryTaskRepository
from task_management.src.usecase.task.task_create_usecase import TaskCreateUseCase


class TestTaskCreateUseCase(unittest.TestCase):
    def test_新規タスクを登録できる(self):
        task_repository = InMemoryTaskRepository()

        usecase = TaskCreateUseCase(task_repository)

        task_id = usecase.create_task('タスクその1', datetime.date(2020, 4, 1))

        # MEMO: postpone_count, task_statusは外から与えられないので、同属性をもつTaskオブジェクトでのアサーションが不可
        #           パターン1: 個々の属性を取り出して、それぞれアサーション
        #                           アサーションルーレットっぽさがあるけど、どういう状態になるかわかりやすい
        # MEMO: task_idはランダムな値になるので、アサーションできなくない？
        #           TaskCreateUseCase.create_task() の中でTaskIdをつくっているので単純には一致させられない
        #               nrs本(C#)では、Idはアサーションしていない
        #           今回はTaskCreateUseCase.create_task() の 返り値 を task_id にしているのでなんとかなる
        #               若干、当たり前だろテストっぽくもあるけど、まあOKとしましょう
        # MEMO: 大事だと思う観点: このテストに重要な情報が過不足なく詰まっているどうか
        #           ドメインモデル図のルールが満たされているか？
        #               ・タスクは「未完了状態」で作成される \
        #               ・タスクは1日延期を3回だけ行うことができる ⇔ 延期回数は初期値0である
        #           ユースケースを満たしているか？
        #               ・タスクを新しく登録できる ⇔ タスク名 と 期限 の一致を確かめる

        actual_task = task_repository.find_by_id(task_id)

        self.assertEqual(task_id, actual_task.task_id)
        self.assertEqual('タスクその1', actual_task.name)
        self.assertEqual(datetime.date(2020, 4, 1), actual_task.due_date)
        self.assertEqual(TaskStatus.UNDONE, actual_task.task_status)
        self.assertEqual(0, actual_task.postpone_count)


if __name__ == '__main__':
    unittest.main()
