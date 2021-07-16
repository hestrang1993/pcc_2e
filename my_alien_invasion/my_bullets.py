# coding=utf-8
"""
The :module:`my_bullets` module will contain the class that handles the player's bullets.
"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    The :class:`Bullet` class extends the :class:`Sprite` class from :module:`pygame.sprite`.
    This class will handle how the player's bullets will behave.
    """

    def __init__(self, alien_invasion):
        """
        Create a new :class:`Ship` instance.

        Parameters
        ----------
        alien_invasion : chapter_12.my_game.my_alien_invasion.AlienInvasion
            The alien invasion game I want to add the ship to.
        """
        super().__init__()
        self.screen = alien_invasion.screen
        self.settings = alien_invasion.settings
        self.bullet_color = self.settings.bullet_color
        self.bullet_rectangle = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        """
        pygame.Rect: The rectangle that defines the bullet's hit box.
        """
        self.bullet_rectangle.midtop = alien_invasion.ship.ship_rectangle.midtop
        self._bullet_y = float(self.bullet_rectangle.y)

    @property
    def bullet_y(self):
        """float: The y-coordinate of the player's bullet."""
        return self._bullet_y

    @bullet_y.setter
    def bullet_y(self, new_bullet_height):
        self._bullet_y = new_bullet_height

    def _get_bullet_rectangle_at_origin(self):
        """
        Create and get a bullet that will spawn at the origin (0, 0) of the screen.

        The bullet's x-coordinate will be adjusted soon after.

        Returns
        -------
        pygame.Rect
            The rectangle that will define the player's bullet.
        """
        width = self.settings.bullet_width
        height = self.settings.bullet_height
        bullet_rectangle = pygame.Rect(0, 0, width, height)
        return bullet_rectangle

    def update(self):
        """
        Update the vertical position of the player's bullet.

        Returns
        -------
        None
        """
        self.bullet_y -= self.settings.bullet_speed
        self.bullet_rectangle.y = self.bullet_y

    def draw_bullet(self):
        """
        Draw the bullet on the screen.

        Returns
        -------
        None
        """
        pygame.draw.rect(self.screen, self.bullet_color, self.bullet_rectangle)
