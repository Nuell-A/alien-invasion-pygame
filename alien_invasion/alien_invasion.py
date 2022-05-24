'''Main file for our game. Will manage and oversee all game mechanics and assets.'''
from argparse import ONE_OR_MORE
import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:
    '''Class to manage overall game assets and behaviors'''

    def __init__(self):
        '''Initialize game and creates game resources'''
        pygame.init()

        self.settings = Settings()
        # Each asset has its own surface which is just a pygame.display the one 
        #   defined below is the surface for the whole game 
        # Creates screen with custom size and lets us use it for the other methods
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        # Sets name of the window that appears
        pygame.display.set_caption("Forisha sucks pp")
        self.ship = Ship(self)
        

    def run_game(self):
        '''Creates main loop for game'''
        while True:
            # Watches keyboard and mouse actions
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            
            # Changes background color during each pass of the for loop
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Makes the most up to date screen visible
            pygame.display.flip()

# Using the if statement below; the game will only run if the alien_invasion.py 
#  file is called (ran) directly
if __name__ == '__main__':
    # Create an instance and run the game.
    ai = AlienInvasion()
    ai.run_game()