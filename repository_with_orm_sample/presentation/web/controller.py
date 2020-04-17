from flask import Flask, jsonify, render_template, request, url_for, redirect

from repository_with_orm_sample.db_config import DB_CONFIG
from repository_with_orm_sample.domain_service.user_domain_service import UserDomainService
from repository_with_orm_sample.infra.orator_user_repository import OratorUserRepository
from repository_with_orm_sample.use_case.domain_exceptions import CanNotRegisterDuplicatedUserException, \
    CanNotRegisterNot20sUserException, CanNotRegisterUserNameException
from repository_with_orm_sample.use_case.fetch_all_user_use_case import FetchAllUserUseCase
from repository_with_orm_sample.use_case.register_user_use_case import RegisterUserUseCae

app = Flask(__name__)


@app.route('/')
def show_users():
    # MEMO: UseCaseのための基本設定は自動でやれるようにしたいよね(フレームワークの使い所？)
    user_repository = OratorUserRepository(DB_CONFIG)
    use_case = FetchAllUserUseCase(user_repository)

    return render_template('index.html', users=use_case.fetch_all_users())


@app.route('/user', methods=['POST'])
def create_user():
    # MEMO: Presentation層としてのValidationがあると思う
    name = request.form['name']
    age = int(request.form['age'])

    # MEMO: UseCaseのための基本設定は自動でやれるようにしたいよね(フレームワークの使い所？)
    user_repository = OratorUserRepository(DB_CONFIG)
    user_domain_service = UserDomainService(user_repository)
    use_case = RegisterUserUseCae(user_repository, user_domain_service)

    # MEMO: 例外処理が汚すぎるのでは！？
    try:
        use_case.create_user(name=name, age=age)
    except (CanNotRegisterNot20sUserException,
            CanNotRegisterUserNameException,
            CanNotRegisterDuplicatedUserException) as e:
        # MEMO: 例外のときはひとまずJSONを返す(書くの面倒だったから)
        return jsonify({'status': e.status_code,
                        'exception': e.__class__.__name__,
                        'message': str(e)})

    return redirect(url_for('show_users'))


if __name__ == '__main__':
    app.run(debug=True)
