from dataclasses import dataclass, InitVar, field
from typing import Dict, List, Optional

from orator import DatabaseManager, Model

from repository_with_orm_sample.domain.domain_user import DomainUser
from repository_with_orm_sample.domain.user_age import UserAge
from repository_with_orm_sample.domain.user_id import UserId
from repository_with_orm_sample.domain.user_name import UserName
from repository_with_orm_sample.domain.user_repository import UserRepository
from repository_with_orm_sample.infra.orator_user import OratorUser


@dataclass
class OratorUserRepository(UserRepository):
    config: InitVar[Dict]
    db: DatabaseManager = field(init=False)

    def __post_init__(self, config: Dict):
        self.db = DatabaseManager(config)
        Model.set_connection_resolver(self.db)

    def register(self, user: DomainUser) -> None:
        orator_user = OratorUser()

        orator_user.id = user.user_id.value
        orator_user.name = user.user_name.value
        orator_user.age = user.user_age.value

        orator_user.save()

    def find_all(self) -> List[DomainUser]:
        orator_users = OratorUser.all()

        domain_users: List[DomainUser] = []

        for orator_user in orator_users:
            domain_user = DomainUser(user_id=UserId.reconstruct(orator_user.id),
                                     user_name=UserName(orator_user.name),
                                     user_age=UserAge(orator_user.age))
            domain_users.append(domain_user)

        return domain_users

    def find_by_name(self, name: str) -> Optional[DomainUser]:
        orator_user = self.db.table('users').where('name', name).first()

        if orator_user is None:
            return None

        return self._to_domain_user(orator_user)

    def find_by_id(self, user_id: UserId) -> Optional[DomainUser]:
        orator_user = OratorUser.find(user_id.value)

        if orator_user is None:
            return None

        return self._to_domain_user(orator_user)

    def _to_domain_user(self, orator_user: OratorUser) -> DomainUser:
        return DomainUser(user_id=UserId.reconstruct(orator_user.id),
                          user_name=UserName(orator_user.name),
                          user_age=UserAge(orator_user.age))
