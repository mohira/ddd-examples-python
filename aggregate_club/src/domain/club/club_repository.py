from abc import ABCMeta, abstractmethod

from aggregate_club.src.domain.club.club import Club
from aggregate_club.src.domain.club.club_id import ClubId


class ClubRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_id(self, club_id: ClubId) -> Club:
        pass

    @abstractmethod
    def save(self, club: Club) -> None:
        pass
