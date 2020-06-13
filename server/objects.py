from typing import Callable, Dict, Optional, Tuple, Union


class Player:

    def __init__(
        self,
        id: int,
        username: str,
        pos: Tuple[float, float],
        score: int = 0,
        send_func: Optional[Callable] = None
    ) -> None:
        self.id = id
        self.username = username
        self.pos = pos
        self.score = score

        if send_func is not None:
            self.send = send_func

    def to_dict(self) -> Dict[str, Union[str, int]]:
        return {
            'id': self.id,
            'username': self.username,
            'pos': self.pos,
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
