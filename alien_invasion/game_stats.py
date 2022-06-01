class GameStats:
    '''Tracks scores in-game'''
    def __init__(self, aigame):
        self.settings = aigame.settings
        self.reset_stats()
        self.high_score = 0
        # Game is inactive by default
        self.game_active = False


    def reset_stats(self):
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
