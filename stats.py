from database import pull_score


class Stats():

    def __init__(self):
        """dnfjnv"""
        self.reset_stats()
        self.run_game = True
        self.high_score = pull_score()[0]

    def reset_stats(self):
        self.guns_left = 2
        self.score = 0

