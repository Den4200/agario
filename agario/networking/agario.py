from typing import Any, Dict

from frost.client.events import EventStatus
from frost.ext import Cog


class Agario(Cog, route='agario'):

    def post_join(data: Dict[str, Any]) -> None:
        EventStatus.join_game = data['headers']['status']

    def post_leave(data: Dict[str, Any]) -> None:
        EventStatus.leave_game = data['jeaders']['status']
