from dataclasses import dataclass


@dataclass
class CircleJoinCommand:
    user_id: str
    circle_id: str
