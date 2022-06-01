import pygame.font
from pygame.sprite import Group
from ship import Ship

class Scoreboard:
    '''Class to display scores in-game'''
    def __init__ (self, aigame):
        self.aigame = aigame
        self.screen = aigame.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = aigame.settings
        self.game_stats = aigame.game_stats

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_ships(self):
        '''Renders ship group on top left'''
        self.ships = Group()
        for ship_number in range(self.game_stats.ships_left):
            ship = Ship(self.aigame)
            ship.rect.x = 10 + ship_number * ship.rect.width
            ship.rect.y = 10
            self.ships.add(ship)

    def prep_level(self):
        '''Renders level image on screen'''
        level_str = str(self.game_stats.level)
        self.level_image = self.font.render(level_str, True, self.text_color,
                self.settings.bg_color)
        
        # Position level below score
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_score(self):
        '''Turns score into rendered image'''
        # Rounds score and adds commas
        # -1 makes it round to the neareast 10 (no decimal)
        rounded_score = round(self.game_stats.score, -1)
        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, 
                self.settings.bg_color)

        # Display score at the top right
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''Renders high score image'''
        high_score = round(self.game_stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
        self.high_score_image = self.font.render(high_score_str, True,
        self.text_color, self.settings.bg_color)
        # Center the high score at the top of the screen.
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def check_high_score(self):
        """Check to see if there's a new high score."""
        if self.game_stats.score > self.game_stats.high_score:
            self.game_stats.high_score = self.game_stats.score
            self.prep_high_score()

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)