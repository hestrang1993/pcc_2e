# coding=utf-8
"""
This module will be where I run the Space Invaders game.
"""
import sys

import pygame

from chapter_12.my_game.my_bullets import Bullet
from chapter_12.my_game.my_ship import Ship
from chapter_12.my_game.settings import Settings


class AlienInvasion:
    """
    The :class:`AlienInvasion` class will manage my game assets and game behaviors.
    """

    def __init__(self):
        """
        Create a new instance of :class:`AlienInvasion`.
        """
        pygame.init()
        self.settings = Settings()
        self._caption_string = "Alien Invasion!"
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption(self.caption_string)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        """
        pygame.sprite.Group: The group of bullets fired by the player's ship.
        """

    @property
    def caption_string(self):
        """
        str: The caption for the game window.
        """
        return self._caption_string

    def run_game(self):
        """
        Start the main loop for the game.

        Returns
        -------
        None
        """
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets_on_screen()
            self._update_the_screen()

    def _check_events(self):
        """
        Watch for keyboard and mouse events that will exit the game.

        Returns
        -------
        None
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_key_down_events(event)
            elif event.type == pygame.KEYUP:
                self._check_key_up_events(event)

    def _check_key_down_events(self, event):
        """
        Handle when the certain keys are pressed down.

        Pressing the arrow keys will move the player ship left or right.
        Pressing the Q key will quit the game.
        Pressing the space bar will fire a bullet.

        Parameters
        ----------
        event : pygame.event.Event
            The pygame handler for specific keyboard events.

        Returns
        -------
        None
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_key_up_events(self, event):
        """
        Handle when the arrow keys and the Q key are released.

        Releasing the arrow keys will stop the player ship from moving left or right.

        Parameters
        ----------
        event : pygame.event.Event
            The pygame handler for specific keyboard events.

        Returns
        -------
        None
        """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        """
        Create a new bullet and add it to the bullet group.

        Returns
        -------
        None
        """
        if len(self.bullets) < self.settings.number_of_bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets_on_screen(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.bullet_rectangle.bottom <= 0:
                self.bullets.remove(bullet)

    def _update_the_screen(self):
        """
        Update the screen periodically.

        Returns
        -------
        None
        """
        self.screen.fill(self.settings.background_color)
        self.ship.blit_me()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
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
