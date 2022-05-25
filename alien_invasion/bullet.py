import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        '''Creates groundwork for the rest of the class.'''
        # Inherit Sprite class attributes/methods by using super()
        super().__init__()

        # Create instances to use in this class
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create bullet rect and then set its position afterwards
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Create decimal value for bullets position
        self.y = float(self.rect.y)

    def update(self):
        '''Moves bullet up across screen'''
        # Update posittion of bullet
        self.y -= self.settings.bullet_speed

        # Sets bullet position
        self.rect.y = self.y

    def draw_bullet(self):
        '''Draws the bullet to the screen'''
        pygame.draw.rect(self.screen, self.color, self.rect)