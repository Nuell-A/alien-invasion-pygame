class Settings:
    '''Class for our game settigns'''

    def __init__(self):
        '''Initialize game settings'''
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed = 1.8

        # Bullet settings
        self.bullet_speed = 1.3
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)