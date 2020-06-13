from typing import Any, Dict

from frost.ext import Cog
from frost.server import auth_required, logger, Memory

from server.headers import Status
from server.objects import GameState, Player
from server.scheduler import Scheduler


class Agario(Cog, route='agario'):

    def __init__(self) -> None:
        Scheduler.schedule(self._send_game_state, 1 / 64, repeat=True)

    @staticmethod
    def _send_game_state() -> None:
        for player in GameState.players:
            player.send({
                'headers': {
                    'path': 'agario/game_state'
                },
                'game_state': GameState.to_dict()
            })

    @auth_required
    def join(
        data: Dict[str, Any],
        token: str,
        id_: str,
        **kwargs: Any
    ) -> None:
        user = Memory.logged_in_users[id_]

        kwargs['client_send']({
            'headers': {
                'path': 'agario/post_join',
                'status': Status.SUCCESS.value
            },
            'game_state': GameState.to_dict()
        })

        GameState.players[id_] = Player(user.id, user.username, (0, 0), kwargs['client_send'])

        logger.info(f'{user.username} joined the game.')

    @auth_required
    def leave(
        data: Dict[str, Any],
        token: str,
        id_: str,
        **kwargs: Any
    ) -> None:
        try:
            GameState.players.pop(id_)

        except KeyError:
            pass

        finally:
            kwargs['client_send']({
                'headers': {
                    'path': 'agario/post_leave',
                    'status': Status.SUCCESS.value
                }
            })

    @auth_required
    def send_pos(
        data: Dict[str, Any],
        token: str,
        id_: str,
        **kwargs: Any
    ) -> None:
        player = GameState.players.get(id_)
        if player is not None:
            player.pos = data['pos']

    @auth_required
    def new_score(
        data: Dict[str, Any],
        token: str,
        id_: str,
        **kwargs: Any
    ) -> None:
        player = Agario.players.get(id_)
        if player is not None:
            player.score = data['score']
