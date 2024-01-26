import pygame.font


class Scores():
    def __init__(self, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats
        self.text_color = (237, 28, 36)
        self.font = pygame.font.SysFont(None, 36)
        self.image_score()
        self.image_high_score()

    def image_score(self):
        self.score_img = self.font.render(str(self.stats.score), True, self.text_color, (0, 0, 0))
        self.score_rect = self.score_img.get_rect()
        self.score_rect.right = self.screen_rect.right - 40
        self.score_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_img, self.score_rect)
        self.screen.blit(self.high_sc_img, self.high_sc_rect)

    def image_high_score(self):
        self.high_sc_img = self.font.render(str(self.stats.high_score), True, self.text_color, (0, 0, 0))
        self.high_sc_rect = self.high_sc_img.get_rect()
        self.high_sc_rect.centerx = self.screen_rect.centerx
        self.high_sc_rect.top = self.screen_rect.top + 20





