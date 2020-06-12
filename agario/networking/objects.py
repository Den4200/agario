from typing import Dict, Union


class Player:

    def __init__(self, id: int, username: str, score: int = 0) -> None:
        self.id = id
        self.username = username
        self.score = score

    def to_dict(self) -> Dict[str, Union[str, int]]:
        return {
            'id': self.id,
            'username': self.username,
            'score': self.score
        }


class GameState:
    players: Dict[int, Player] = dict()

    @classmethod
    def to_dict(cls) -> str:
        return {
            'players': [
                player.to_dict() for player in cls.players
            ]
        }

    @classmethod
    def from_dict(cls, data) -> None:
        cls.players = {
            p['id']: Player(**p) for p in data['players']
        }
