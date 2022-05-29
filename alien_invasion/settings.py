class Settings:
    '''Class for our game settigns'''

    def __init__(self):
        '''Initialize game settings'''
        # Screen settings
        self.screen_width = 1280
        self.screen_height = 720
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 300
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 5

        # Alien settings
        self.fleet_drop_speed = 10

        # How fast game scales
        self.speedup_scale = 1.1
        self.score_scale = 1.5

        self.dynamic_settings()

    def dynamic_settings(self):
        # Alien settings
        self.alien_speed = 3
        # Fleet direction 1 is right and -1 is left
        self.fleet_direction = 1

        # Bullet
        self.bullet_speed = 5

        # Ship
        self.ship_speed = 3.5

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        '''Increases difficulte (speed) and value of aliens shot'''
        self.alien_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.ship_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
        

