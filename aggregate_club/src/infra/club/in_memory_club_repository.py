from dataclasses import dataclass
from typing import Dict

from aggregate_club.src.domain.club.club import Club
from aggregate_club.src.domain.club.club_id import ClubId
from aggregate_club.src.domain.club.club_repository import ClubRepository


@dataclass
class InMemoryClubRepository(ClubRepository):
    data_dict: Dict[ClubId, Club]

    def find_by_id(self, club_id: ClubId) -> Club:
        return self.data_dict[club_id]

    def save(self, club: Club) -> None:
        self.data_dict[club.club_id] = club
