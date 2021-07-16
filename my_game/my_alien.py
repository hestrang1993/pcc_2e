# coding=utf-8
"""
The :module:`alien` will handle the behaviors and characteristics of the alien NPCs.

This will be done through the :class:`Alien`, which extends :class:`pygame.sprite.Sprite`.
"""
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """
    The :class:`Alien` will handle the behaviors and characteristics of the alien NPCs.
    """

    def __init__(self, alien_invasion):
        """
        Create a new :class:`Alien` instance.

        Parameters
        ----------
        alien_invasion: chapter_12.my_game.my_alien_invasion.AlienInvasion
            The alien invasion game I want to add the ship to.
        """
        super().__init__()
        self.screen = alien_invasion.screen
        self._alien_image_file_path = 'images/alien_resized.png'
        self._alien_image = pygame.image.load(self.alien_image_file_path)
        self.alien_rectangle = self.alien_image.get_rect()
        """
        pygame.Rect: The hit box for the alien NPC sprites.
        """
        self.alien_rectangle.x = self.alien_rectangle.width
        self.alien_rectangle.y = self.alien_rectangle.height
        self.alien_x = float(self.alien_rectangle.x)
        """
        float: The x-position of an aline NPC sprite.
        """

        # Needed to load in the images correctly.
        self.image = self.alien_image
        self.rect = self.alien_rectangle

    @property
    def alien_image_file_path(self):
        """str: The file path to the image for the alien NPCs."""
        return self._alien_image_file_path

    @property
    def alien_image(self):
        """pygame.Surface: The image to use for the alien NPC sprites."""
        return self._alien_image
