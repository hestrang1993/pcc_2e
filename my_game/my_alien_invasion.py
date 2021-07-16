# coding=utf-8
"""
This module will be where I run the Space Invaders game.
"""
import sys

import pygame

from my_alien import Alien
from my_bullets import Bullet
from my_ship import Ship
from settings import Settings


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
        self.aliens = pygame.sprite.Group()
        """
        pygame.sprite.Group: The group of alien NPC sprites.
        """
        self._create_fleet()

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
        """
        Keep track of how many bullets are on screen.

        Returns
        -------
        None
        """
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
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _get_max_n_of_aliens_per_row(self, alien_instance):
        """
        Get the maximum number of aliens that can be added per row in the game window.

        Parameters
        ----------
        alien_instance : my_game.my_alien.Alien
            The alien NPC sprite.

        Returns
        -------
        int
            The maximum number of aliens allowed per row.
        """
        alien_width = alien_instance.rect.width
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_of_aliens_in_a_row = available_space_x // (2 * alien_width)
        return number_of_aliens_in_a_row

    def _get_max_n_of_rows_of_aliens(self, alien_instance):
        """
        Get the maximum number of rows of aliens that can be added in the game window.

        Parameters
        ----------
        alien_instance : my_game.my_alien.Alien
            The alien NPC sprite.

        Returns
        -------
        int
            The maximum number of rows of aliens to add to the game.
        """
        alien_height = alien_instance.rect.height
        ship_height = self.ship.ship_rectangle.height
        distance = (16 * alien_height) - ship_height
        available_space_y = self.settings.screen_height - distance
        number_of_rows_of_aliens = available_space_y // (2 * alien_height)
        return number_of_rows_of_aliens

    def _create_alien(self, column_number, row_number):
        """
        Create an alien that will spawn into a specific row and column into the game window.

        Parameters
        ----------
        column_number : int
            The column within a row to add the alien to.
        row_number : int
            The row to add the alien to.

        Returns
        -------
        None
        """
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * column_number
        alien.rect.x = alien.x
        product = alien.rect.height * row_number
        alien.rect.y = alien.rect.height + (2 * product)
        self.aliens.add(alien)

    def _add_aliens_to_row(self, number_of_rows, number_of_aliens_per_row):
        """
        Add the max number of alien sprites allowed per row.

        Parameters
        ----------
        number_of_rows : int
            The maximum number of rows of aliens.
        number_of_aliens_per_row : int
            The maximum number of aliens allowed per row.

        Returns
        -------
        None
        """
        for row in range(number_of_rows):
            for column in range(number_of_aliens_per_row):
                self._create_alien(column, row)

    def _create_fleet(self):
        """
        Create a fleet of :class:`Alien` NPCs.

        Returns
        -------
        None
        """
        alien = Alien(self)
        number_of_aliens_per_row = self._get_max_n_of_aliens_per_row(alien)
        number_of_rows_of_aliens = self._get_max_n_of_rows_of_aliens(alien)
        self._add_aliens_to_row(number_of_rows_of_aliens, number_of_aliens_per_row)


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
