import pygame.font


class Button:
    def __init__(self, aigame, ):
        '''Initialize attributes'''
        self.screen = aigame.screen
        self.screen_rect = self.screen.get_rect()

        # Set button settings
        self.button_width, self.button_height = 50, 30
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)

        # Build buttons rect
        self.rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.rect.center = self.screen_rect.center
