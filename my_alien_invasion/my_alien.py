# coding=utf-8
"""
The :module:`alien` will handle the behaviors and characteristics of the alien NPCs.

This will be done through the :class:`Alien`, which extends :class:`pygame.sprite.Sprite`.
"""
from pygame.sprite import Sprite


class Alien(Sprite):

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
        self.alien_image = None
