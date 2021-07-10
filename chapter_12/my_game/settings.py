# coding=utf-8
"""
The :module:`my_settings` module contains many of the settings I will need to play the game.
"""


class Settings:
    """The :class:`Settings` stores all the settings for my version of Alien Invasion."""

    def __init__(self):
        self._screen_width = 1200
        self._screen_height = 800
        self._screen_dimensions = (self.screen_width, self.screen_height)
        self._background_color_channel_value = 0
        self._background_color = (
                self.background_color_channel_value,
                self.background_color_channel_value,
                self.background_color_channel_value
        )
        self._ship_speed = 1.5
        self._bullet_speed = 1.0
        self._bullet_width = 4
        self._bullet_height = 16
        self._bullet_color_channel_value = 255
        self._bullet_color = (
                self.bullet_color_channel_value,
                self._bullet_color_channel_value,
                self.bullet_color_channel_value
        )

    @property
    def screen_width(self):
        """int: The pixel width of the screen."""
        return self._screen_width

    @screen_width.setter
    def screen_width(self, width):
        self._screen_width = width

    @property
    def screen_height(self):
        """int: The pixel height of the screen."""
        return self._screen_height

    @screen_height.setter
    def screen_height(self, height):
        self._screen_height = height

    @property
    def screen_dimensions(self):
        """tuple[int, int]: The pixel width and height of the screen, respectively."""
        return self._screen_dimensions

    @property
    def background_color_channel_value(self):
        """int: The value for each RGB channel."""
        return self._background_color_channel_value

    @property
    def background_color(self):
        """tuple[int, int, int]: The background color for the game window."""
        return self._background_color

    @property
    def ship_speed(self):
        """float: The horizontal speed of the player."""
        return self._ship_speed

    @property
    def bullet_speed(self):
        """float: The vertical speed of the player's bullets, in pixels per cycle."""
        return self._bullet_speed

    @property
    def bullet_width(self):
        """int: The pixel width of the player's bullets."""
        return self._screen_width

    @property
    def bullet_height(self):
        """int: The pixel height of the player's bullets."""
        return self._bullet_height

    @property
    def bullet_color_channel_value(self):
        """int: The value for all RGB channels for the player's bullets."""
        return self._bullet_color_channel_value

    @property
    def bullet_color(self):
        """tuple[int, int, int]: The RGB coloring for the player's bullets."""
        return self._bullet_color
