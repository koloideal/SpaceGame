import pygame
from gun import Gun
import controls
from pygame.sprite import Group
from stats import Stats


def run():

    pygame.init()
    screen = pygame.display.set_mode((700, 800))
    pygame.display.set_caption('SpaceGame')
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    controls.create_army(screen, inos)
    stats = Stats()

    while True:

        controls.events(screen, gun, bullets)
        gun.update_gun()
        controls.update_bullets(screen, inos, bullets)

        controls.update_inos(stats, screen, gun, inos, bullets)
        controls.update(bg_color, screen, gun, inos, bullets)


run()
