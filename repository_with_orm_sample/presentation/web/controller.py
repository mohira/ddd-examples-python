from flask import Flask, render_template

from repository_with_orm_sample.db_config import DB_CONFIG
from repository_with_orm_sample.infra.orator_user_repository import OratorUserRepository
from repository_with_orm_sample.use_case.fetch_all_user_use_case import FetchAllUserUseCase

app = Flask(__name__)


@app.route('/')
def show_users():
    # MEMO: UseCaseのための基本設定は自動でやれるようにしたいよね(フレームワークの使い所？)
    user_repository = OratorUserRepository(DB_CONFIG)
    use_case = FetchAllUserUseCase(user_repository)

    return render_template('index.html', users=use_case.fetch_all_users())


if __name__ == '__main__':
    app.run(debug=True)
