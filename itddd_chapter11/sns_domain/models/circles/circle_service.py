from dataclasses import dataclass

from itddd_chapter11.sns_domain.models.circles.circle import Circle
from itddd_chapter11.sns_domain.models.circles.i_circle_repository import ICircleRepository


@dataclass
class CircleService:
    circle_repository: ICircleRepository

    def exists(self, circle: Circle) -> bool:
        duplicated = self.circle_repository.find_by_name(circle.name)

        return duplicated is not None
