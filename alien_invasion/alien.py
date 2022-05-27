import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    '''This class represents a single alien'''
    def __init__(self, ai_game):
        super().__init__()
        # Get screen, settings and rect size from AlienInvasion
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load alien
        self.image = pygame.image.load('alien_invasion/assets/alien.bmp')
        self.rect = self.image.get_rect()

        # Start alien near the top left
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Lets us use decimal values for position
        self.x = float(self.rect.x)

    def update(self):
        '''Moves aliens'''
        self.x += (self.settings.alien_speed *
                    self.settings.fleet_direction)
        self.rect.x = self.x

    def check_edges(self):
        '''Returns true if alien is at the edge of the screen'''
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    

