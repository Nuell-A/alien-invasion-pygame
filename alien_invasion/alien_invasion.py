'''Main file for our game. Will manage and oversee all game mechanics and assets.'''
from argparse import ONE_OR_MORE
from re import S
import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

# The following allows you to play in fullscreen
# self.screen = pygame.display.set_mode(
#     (0,0), pygame.FULLSCREEN)
# self.screen_width = self.screen.get_rect().width
# self.screen_height = self.screen.get_rect().height

class AlienInvasion:
    '''Class to manage overall game assets and behaviors'''

    def __init__(self):
        '''Initialize game and creates game resources'''
        pygame.init()

        self.settings = Settings()
        # Every object has its own surface (rect/display), we can also create our own surface
        self.screen = pygame.display.set_mode((self.settings.screen_width, 
            self.settings.screen_height))
        pygame.display.set_caption("Forisha sucks pp")
        self.game_stats = GameStats(self)

        # A Group() is a list with added functionality
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        # Calls other modules and passes 'self' to create an instance of itself in the the other modules
        self.ship = Ship(self)
        self._create_fleet()
        self.play_button = Button(self, 'Play')
        self.scoreboard = Scoreboard(self)

    def _update_screen(self):
        '''Updates game screen'''
        # Changes background color during each pass of the for loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)
        self.scoreboard.show_score()

        # Draws button if game is inactive
        if not self.game_stats.game_active:
            self.play_button.draw_button()
        
        # Makes the most up to date screen visible
        pygame.display.flip()

    def run_game(self):
        '''Creates main loop for game'''
        while True:
            self._check_events()
            if self.game_stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_alien_bottom(self):
        '''Checks if an alien reaches the bottom of the screen'''
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_aliens(self):
        '''Updates positions of the whole fleet
        and checks if they are at an edge.'''
        self.aliens.update()
        self._check_fleet_edges()

        # Checks for ship, alien collsion
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        self._check_alien_bottom()

    def _ship_hit(self):
        '''When ship gets hit; gets rid of aliens, bullets and re-centers ship. 
        Also pauses the game for 0.5 secs'''
        if self.game_stats.ships_left > 0:
            # Empties sprites
            self.bullets.empty()
            self.aliens.empty()

            # Creates new fleet and recenters ship
            self._create_fleet()
            self.ship.center_ship()
            # Decrements ship lives
            self.game_stats.ships_left -= 1
            # Pauses
            sleep(0.5)
        else:
            self.game_stats.game_active = False
            pygame.mouse.set_visible(True)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_directions()
                break

    def _change_fleet_directions(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _create_fleet(self):
        '''Create the fleet of aliens'''
        # Find out how many aliens fit in one screen with one aliens width between them
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # How many rows fit on the screen
        ship_height = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # Create row of aliens
        for row in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row)

    def _create_alien(self, alien_number, row):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien_height * row
        self.aliens.add(alien)    

    def _update_bullets(self):
        '''Updates position of bullets'''
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
        self._check_bullet_collision()

    def _check_bullet_collision(self):
        '''Checks alien, bullet collision and creates new fleet if necessary'''
        # Adds collision between to sprites. True makes it so that those objects disappear
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

        if collisions:
            for aliens in collisions.values():
                self.game_stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()

        # Checks if alien fleet is destroyed and creates new one while emptying the bullet list.
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

    def _fire_bullet(self):
        '''Adds bullets to the group'''
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    # Using a single leading underscore marks the method/vairable/function as a weak private
    def _check_events(self):
        '''Watches keyboard and mouse actions'''
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_pos):
        '''Starts new game when player clicks play'''
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_stats.game_active:
            # Resets dynamic settings and starts the game
            self.settings.dynamic_settings()
            self.game_stats.reset_stats()
            self.game_stats.game_active = True

            # Gets rid of aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            # Creates new fleet and centers ship
            self._create_fleet()
            self.ship.center_ship()

            self.scoreboard.prep_score()

            pygame.mouse.set_visible(False)

    def _keydown_events(self, event):
        '''Tracks key presses'''
        if event.key == pygame.K_d:
            self.ship.moving_right = True
        elif event.key == pygame.K_a:
            self.ship.moving_left = True
        elif event.key == pygame.K_s:
            self.ship.moving_down = True
        elif event.key == pygame.K_w:
            self.ship.moving_up = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_q:
            sys.exit()


    def _keyup_events(self, event):
        '''Tracks key releases'''
        if event.key == pygame.K_d:
            self.ship.moving_right = False
        elif event.key == pygame.K_a:
            self.ship.moving_left = False
        elif event.key == pygame.K_s:
            self.ship.moving_down = False
        elif event.key == pygame.K_w:
            self.ship.moving_up = False

            

# Using the if statement below; the game will only run if the alien_invasion.py 
#  file is called (ran) directly
if __name__ == '__main__':
    # Create an instance and run the game.
    ai = AlienInvasion()
    ai.run_game()