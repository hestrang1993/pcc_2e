# coding=utf-8
"""
The :module:`my_ship` module will manage my ship and its controls.
"""
import pygame


class Ship:
    """
    The :class:`Ship` class manages the player's ship.
    """

    def __init__(self, alien_invasion):
        """
        Create a new :class:`Ship` instance.

        Parameters
        ----------
        alien_invasion : chapter_12.my_game.my_alien_invasion.AlienInvasion
            The alien invasion game I want to add the ship to.
        """
        self.ship_image_file_pathg = None
        self.screen = alien_invasion.screen
        """
        pygame.Surface: The screen to display the game on.
        """
        self.ship_settings = alien_invasion.settings
        """
        chapter_12.my_game.settings.Settings: An attribute that accesses the ship's settings from the Settings module.
        """
        self.screen_rectangle = alien_invasion.screen.get_rect()
        """
        pygame.Rect: The rectangle for the game window.
        """
        self._ship_image_file_path = 'images/ship_resized.png'
        self.ship_image = pygame.image.load(self.ship_image_file_path)
        """
        pygame.Surface: The ship_image of the player's ship.
        """
        self.ship_rectangle = self.ship_image.get_rect()
        """
        pygame.Rect: The rectangle for the ship_image that will serve as the player's ship.'
        """
        self.ship_rectangle.midbottom = self.screen_rectangle.midbottom

        self._ship_x = float(self.ship_rectangle.x)

        self._moving_right = False
        self._moving_left = False

    @property
    def ship_image_file_path(self):
        """
        str: The file path to the ship_image that will serve as the player's ship.
        """
        return self._ship_image_file_path

    @property
    def moving_right(self):
        """
        bool: The flag for whether the player is moving right.
        """
        return self._moving_right

    @moving_right.setter
    def moving_right(self, flag):
        self._moving_right = flag

    @property
    def moving_left(self):
        """
        bool: The flag for whether the player is moving left.
        """
        return self._moving_left

    @moving_left.setter
    def moving_left(self, flag):
        self._moving_left = flag

    @property
    def ship_x(self):
        """
        float: The x-position of the player's ship.
        """
        return self._ship_x

    @ship_x.setter
    def ship_x(self, new_position):
        self._ship_x = new_position

    def _move_ship_right(self):
        """
        Move the ship right on the screen until it hits the right edge of the screen.

        Returns
        -------
        None
        """
        if self.moving_right and self.ship_rectangle.right < self.screen_rectangle.right:
            self.ship_x += self.ship_settings.ship_speed

    def _move_ship_left(self):
        """
        Move the ship left on the screen until it hits the left edge of the screen.

        Returns
        -------
        None
        """
        if self.moving_left and self.ship_rectangle.left > 0:
            self.ship_x -= self.ship_settings.ship_speed

    def update(self):
        """
        Move the ship left or right continuously until the player hits the edge of the screen.

        Returns
        -------
        None
        """
        self._move_ship_right()
        self._move_ship_left()
        self.ship_rectangle.x = self.ship_x

    def blit_me(self):
        """
        Draw the ship at its current position.

        Returns
        -------
        None
        """
        self.screen.blit(self.ship_image, self.ship_rectangle)
