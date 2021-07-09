# coding=utf-8
"""
This module will be where I run the Space Invaders game.
"""
import sys

import pygame


class AlienInvasion:
    """
    The :class:`AlienInvasion` class will manage my game assets and game behaviors.
    """

    def __init__(self):
        """
        Create a new instance of :class:`AlienInvasion`.
        """
        pygame.init()
        self.screen_dimension = (1200, 800)
        self.screen = pygame.display.set_mode(self.screen_dimension)

    @staticmethod
    def _watch_for_keyboard_and_mouse_events():
        """
        Watch for keyboard and mouse events that will exit the game.

        Returns
        -------
        None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

    def run_game(self):
        """
        Start the main loop for the game.
        """
        self._watch_for_keyboard_and_mouse_events()
        pygame.display.flip()


def main():
    """
    Make a new game instance and then run the game.

    Returns
    -------
    None
    """
    alien_invasion = AlienInvasion()
    alien_invasion.run_game()


if __name__ == '__main__':
    main()
