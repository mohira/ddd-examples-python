from orator import DatabaseManager, Schema
from orator.schema import Blueprint

from repository_with_orm_sample.db_config import DB_CONFIG


def main():
    """
    usersテーブルを作成する

    | カラム | データ型 |
    | ------ | -------- |
    | id     | VARCHAR  |
    | name   | VARCHAR  |
    | age    | INTEGER  |
    """
    db = DatabaseManager(DB_CONFIG)
    schema = Schema(db)

    TABLE_NAME = 'users'

    schema.drop_if_exists(TABLE_NAME)

    with schema.create(TABLE_NAME) as table:
        table: Blueprint
        table.string('id').unique()
        table.string('name')
        table.integer('age')


if __name__ == '__main__':
    main()
