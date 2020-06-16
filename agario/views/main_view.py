import arcade
from arcade_ui import EventMap, TextButton, View

from agario import Settings as s


class LoginButton(TextButton):
    __widget_name__ = 'login_button'

    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx

    def on_submit(self):
        self.ctx.login()


class RegisterButton(TextButton):
    __widget_name__ = 'register_button'

    def __init__(self, ctx, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.ctx = ctx

    def on_submit(self):
        self.ctx.register()


class MainView(View):

    def __init__(self, event_map: EventMap) -> None:
        super().__init__(event_map)

        self.title = None
        self.login_button = None
        self.register_button = None

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def on_show(self) -> None:
        self.event_map.clear()

        self.title = arcade.draw_text(
            text=s.NAME,
            start_x=s.WINDOW_SIZE[0] / 2,
            start_y=s.WINDOW_SIZE[1] / 8 * 7,
            color=arcade.color.WHITE,
            font_size=32,
            align='center',
            anchor_x='center',
            anchor_y='center'
        )

        self.login_button = LoginButton(
            ctx=self,
            text='Login',
            center_x=s.WINDOW_SIZE[0] / 2 - 75,
            center_y=s.WINDOW_SIZE[1] / 2,
            width=100,
            height=25,
            border_width=3,
            viewport=[0, 0]
        )

        self.register_button = RegisterButton(
            ctx=self,
            text='Register',
            center_x=s.WINDOW_SIZE[0] / 2 + 75,
            center_y=s.WINDOW_SIZE[1] / 2,
            width=100,
            height=25,
            border_width=3,
            viewport=[0, 0]
        )

        super().setup()

    def on_draw(self) -> None:
        arcade.start_render()

        self.title.draw()

        self.login_button.draw()
        self.register_button.draw()

    def login(self) -> None:
        pass

    def register(self) -> None:
        pass
