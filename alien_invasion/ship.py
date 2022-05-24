import pygame

class Ship:
    '''This class will handle the ships functions'''
    def __init__(self, ai_game): # ai_game would be an instance of AlienInvasion
        '''Initialize ship and set its starting position'''
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()

        # Load ship image and get its rect
        self.image = pygame.image.load('alien_invasion/assets/ship.bmp')
        self.rect = self.image.get_rect()

        # Start a new ship in the bottom-middle
        self.rect.midbottom = self.screen_rect.midbottom


    def blitme(self):
        '''Draws the ship at its current location'''
        self.screen.blit(self.image, self.rect)