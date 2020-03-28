from dataclasses import dataclass

from repository_with_orm_sample.db_config import DB_CONFIG
from repository_with_orm_sample.domain.user_repository import UserRepository
from repository_with_orm_sample.infra.orator_user_repository import OratorUserRepository


@dataclass
class DisplayAllUserUseCase:
    """Presentation層の役目かもしれないね"""
    user_repository: UserRepository

    def display_all_users_as_csv(self) -> None:
        domain_users = self.user_repository.find_all()

        for domain_user in domain_users:
            print(domain_user.as_csv())


def main():
    user_repository = OratorUserRepository(DB_CONFIG)
    use_case = DisplayAllUserUseCase(user_repository)

    use_case.display_all_users_as_csv()


if __name__ == '__main__':
    main()
