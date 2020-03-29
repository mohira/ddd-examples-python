from abc import ABCMeta, abstractmethod

from itddd_chapter11.sns_domain.models.circles.circle import Circle
from itddd_chapter11.sns_domain.models.circles.circle_id import CircleId
from itddd_chapter11.sns_domain.models.circles.circle_name import CircleName


class ICircleRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, circle: Circle) -> None:
        pass

    @abstractmethod
    def find_by_id(self, circle_id: CircleId) -> Circle:
        pass

    @abstractmethod
    def find_by_name(self, circle_name: CircleName) -> Circle:
        pass
