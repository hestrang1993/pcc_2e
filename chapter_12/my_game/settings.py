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
        self._channel_value = 0
        self._background_color = (self.channel_value, self.channel_value, self.channel_value)

    @property
    def screen_width(self):
        """int: The pixel width of the screen."""
        return self._screen_width

    @property
    def screen_height(self):
        """int: The pixel height of the screen."""
        return self._screen_height

    @property
    def screen_dimensions(self):
        """tuple[int, int]: The pixel width and height of the screen, respectively."""
        return self._screen_dimensions

    @property
    def channel_value(self):
        """int: The value for each RGB channel."""
        return self._channel_value

    @property
    def background_color(self):
        """tuple[int, int, int]: The background color for the game window."""
        return self._background_color
