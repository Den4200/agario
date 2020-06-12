from typing import Tuple

from frost import FrostClient
from frost.client import get_auth

from agario.networking.agario import Agario


class Client(FrostClient):

    def __init__(self, ip: str = '127.0.0.1', port: int = 5555) -> None:
        super().__init__(ip, port)

        # Load up cogs
        Agario()

    @get_auth
    def new_pos(self, pos: Tuple[int, int], token: str, id_: str) -> None:
        self.send({
            'headers': {
                'path': 'agario/new_pos',
                'id': id_,
                'token': token
            },
            'pos': pos
        })

    @get_auth
    def new_score(self, score: int, token: str, id_: str) -> None:
        self.send({
            'headers': {
                'path': 'agario/new_score',
                'id': id_,
                'token': token
            },
            'score': score
        })

    @get_auth
    def join_game(self, token: str, id_: str) -> None:
        self.send({
            'headers': {
                'path': 'agario/join',
                'token': token,
                'id': id_
            }
        })

    @get_auth
    def leave_game(self, token: str, id_: str) -> None:
        self.send({
            'headers': {
                'path': 'multiplayer/leave',
                'token': token,
                'id': id_
            }
        })
