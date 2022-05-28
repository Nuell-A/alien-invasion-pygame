import pygame

class Ship:
    '''This class will handle the ships functions'''
    def __init__(self, ai_game): # ai_game would be an instance of AlienInvasion
        '''Initialize ship and set its starting position'''
        self.screen = ai_game.screen 
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        # Load ship image and get its rect
        self.image = pygame.image.load('alien_invasion/assets/ship.bmp')
        self.rect = self.image.get_rect()

        # Start a new ship in the bottom-middle
        self.rect.midbottom = self.screen_rect.midbottom

        # Flags for movement
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        # Storing a decimal value for the ship for finer control
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        '''Decides ships movement based on self.moving_right (True or False)'''
        # Here we update the ships x value not the rect.
        #  Also keeps the image from going past the edges. 
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        # Sets ships rect value to the x value (wihout this the rect (ship) wouldn't move)
        self.rect.x = self.x
        self.rect.y = self.y
        
        
    def blitme(self):
        '''Draws the ship at its current location'''
        self.screen.blit(self.image, self.rect)

    def center_ship(self):
        '''Re-centers ship when this method is called.'''
        self.rect.midbottom = self.screen_rect.midbottom
        # Resets the ship's x and y positions 
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)