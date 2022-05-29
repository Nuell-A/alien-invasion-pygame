import pygame.font

class Scoreboard:
    '''Class to display scores in-game'''
    def __init__ (self, aigame):
        self.screen = aigame.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = aigame.settings
        self.game_stats = aigame.game_stats

        # Font settings
        self.text_color = (30, 30, 30)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()

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

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)