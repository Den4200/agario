import arcade
from arcade_ui import EventMap

from agario import Settings as s
from agario.views import MainView


def main() -> None:
    window = arcade.Window(*s.WINDOW_SIZE, s.NAME)
    event_map = EventMap()

    window.show_view(MainView(event_map))
    arcade.run()


if __name__ == "__main__":
    main()
