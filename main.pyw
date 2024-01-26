import pygame
from utils.gun import Gun
from utils import controls
from pygame.sprite import Group
from utils.stats import Stats
from utils.scores import Scores


def run():

    pygame.init()
    screen = pygame.display.set_mode((850, 800))
    pygame.display.set_caption('SpaceGame')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:

        controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            controls.update_bullets(screen, stats, sc, inos, bullets)

            controls.update_inos(stats, screen, sc, gun, inos, bullets)
            controls.update(bg_color, screen, stats, sc, gun, inos, bullets)


run()
