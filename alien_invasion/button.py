import pygame.font


class Button:
    def __init__(self, aigame, msg):
        '''Initialize attributes'''
        self.screen = aigame.screen
        self.screen_rect = self.screen.get_rect()

        # Set button settings
        self.button_width, self.button_height = 50, 30
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        # None tells python to use default font and 48 is the size of the font
        self.font = pygame.font.SysFont(None, 48)

        # Build buttons rect
        self.rect = pygame.Rect(0, 0, self.button_width, self.button_height)
        self.rect.center = self.screen_rect.center

        self._prep_msg(msg)

    def _prep_msg(self, msg):
        '''Renders your button with all the information required'''
        # render() takes the message, a boolean value for anti-aliasing on or off, then 
        self.msg_image = self.font.render(msg, True, self.text_color, 
            self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        '''Fills and inserts text in button'''
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)