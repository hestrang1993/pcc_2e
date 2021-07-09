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
        self.screen = alien_invasion.screen
        """
        pygame.Surface: The screen to display the game on.
        """
        self.screen_rectangle = alien_invasion.screen.get_rect()
        """
        pygame.Rect: The rectangle for the game window.
        """
        self._ship_image_file_path = 'images/background.png'
        self.image = pygame.image.load("images/background.png")
        """
        pygame.Surface: The image of the player's ship.
        """
        self.image_rectangle = self.image.get_rect()
        """
        pygame.Rect: The rectangle for the image that will serve as the player's ship.'
        """
        self.image_rectangle.midbottom = self.screen_rectangle.midbottom

    @property
    def ship_image_file_path(self):
        """
        str: The file path to the image that will serve as the player's ship.
        """
        return self._ship_image_file_path

    def blit_me(self):
        """
        Draw the ship at its current position.

        Returns
        -------
        None
        """
        self.screen.blit(self.image, self.image_rectangle)
