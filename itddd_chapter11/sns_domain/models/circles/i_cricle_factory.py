from abc import ABCMeta, abstractmethod

from itddd_chapter11.sns_domain.models.circles.circle import Circle
from itddd_chapter11.sns_domain.models.circles.circle_name import CircleName
from itddd_chapter11.sns_domain.models.users.user import User


class ICircleFactory(metaclass=ABCMeta):
    @abstractmethod
    def create(self, circle_name: CircleName, owner: User) -> Circle:
        pass
