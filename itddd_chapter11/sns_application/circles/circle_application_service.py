from dataclasses import dataclass

from itddd_chapter11.sns_application.circles.can_not_register_circle_exception import CanNotRegisterCircleException
from itddd_chapter11.sns_application.circles.circle_full_exception import CircleFullException
from itddd_chapter11.sns_application.circles.circle_not_found_exception import CircleNotFoundException
from itddd_chapter11.sns_application.circles.create.circle_create_command import CircleCreateCommand
from itddd_chapter11.sns_application.circles.join.circle_join_command import CircleJoinCommand
from itddd_chapter11.sns_application.users.user_not_found_exception import UserNotFoundException
from itddd_chapter11.sns_domain.models.circles.circle_id import CircleId
from itddd_chapter11.sns_domain.models.circles.circle_name import CircleName
from itddd_chapter11.sns_domain.models.circles.circle_service import CircleService
from itddd_chapter11.sns_domain.models.circles.i_circle_repository import ICircleRepository
from itddd_chapter11.sns_domain.models.circles.i_cricle_factory import ICircleFactory
from itddd_chapter11.sns_domain.models.users.i_user_repository import IUserRepository
from itddd_chapter11.sns_domain.models.users.user_id import UserId


@dataclass
class CircleApplicationService:
    circle_factory: ICircleFactory
    circle_repository: ICircleRepository
    user_repository: IUserRepository
    circle_service: CircleService

    def create(self, command: CircleCreateCommand) -> None:
        """サークルを作成する
        # MEMO: Transactionは省略
        """

        # サークルを作成するために、サークルのオーナーであるユーザの検索
        owner_id = UserId(command.user_id)
        owner = self.user_repository.find_by_id(owner_id)

        # ユーザの存在を確認
        if owner is None:
            raise UserNotFoundException(f'{owner_id} サークルのオーナーとなるユーザが見つかりませんでした。')

        # サークルの生成
        name = CircleName(command.name)
        circle = self.circle_factory.create(name, owner)

        # サークル名の重複チェック
        if self.circle_service.exists(circle):
            raise CanNotRegisterCircleException(f'{circle} サークルは既に存在しています。')

        # 永続化
        self.circle_repository.save(circle)

    def join(self, command: CircleJoinCommand) -> None:
        """サークルに参加する
        # MEMO: Transactionは省略
        """

        member_id = UserId(command.user_id)
        member = self.user_repository.find_by_id(member_id)

        if member is None:
            raise UserNotFoundException(f'{member_id} ユーザが見つかりませんでした。')

        circle_id = CircleId(command.circle_id)
        circle = self.circle_repository.find_by_id(circle_id)

        if circle is None:
            raise CircleNotFoundException(f'{circle} サークルが見つかりませんでした。')

        # サークルのオーナーを含めて30名か確認
        # Refactor: 29なのか30なのか分かりづらい！
        # Refactor: このコードが散らかっちゃう！
        if len(circle.members) >= 29:
            raise CircleFullException(f'{circle_id}')

        circle.members.append(member)

        self.circle_repository.save(circle)
