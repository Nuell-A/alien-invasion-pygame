'''Main file for our game. Will manage and oversee all game mechanics and assets.'''
from argparse import ONE_OR_MORE
import sys
import pygame
from settings import Settings
from ship import Ship
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
        # Each asset has its own surface which is just a pygame.display the one 
        #   defined below is the surface for the whole game 
        # Creates screen with custom size and lets us use it for the other methods
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        # Sets name of the window that appears
        pygame.display.set_caption("Forisha sucks pp")

        # Calls ship.py and gives self as an instance
        self.ship = Ship(self)
        

    def run_game(self):
        '''Creates main loop for game'''
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()


    def _update_screen(self):
        '''Updates game screen'''
        # Changes background color during each pass of the for loop
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        

        # Makes the most up to date screen visible
        pygame.display.flip()


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