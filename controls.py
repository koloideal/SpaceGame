import pygame
import sys
from bullet import Bullet
from ino import Ino
import time


def events(screen, gun, bullets):
    """обработка событий"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                gun.mleft = True

            elif event.key == pygame.K_d:
                gun.mright = True

            elif event.key == pygame.K_SPACE:
                new_bullet = Bullet(screen, gun)
                bullets.add(new_bullet)

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                gun.mleft = False

            if event.key == pygame.K_d:
                gun.mright = False


def update(bg_color, screen, stats, sc, gun, inos, bullets):
    screen.fill(bg_color)
    sc.show_score()
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    gun.output()
    inos.draw(screen)
    pygame.display.flip()


def update_bullets(screen, stats, sc, inos, bullets):
    """обновлять позиции пуль"""
    bullets.update()
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    collision = pygame.sprite.groupcollide(bullets, inos, True, True)
    if collision:
        for ino in collision.values():
            stats.score += 10 * len(ino)
        sc.image_score()
        check_high_score(stats, sc)
    if len(inos) == 0:
        bullets.empty()
        create_army(screen, inos)


def create_army(screen, inos):
    ino = Ino(screen)
    ino_width = ino.rect.width
    number_ino_x = int((700 - 2 * ino_width) / ino_width)

    ino_height = ino.rect.height
    number_ino_y = int((800 - 100 - 2 * ino_height) / ino_height)

    for row_number in range(number_ino_y - 10):
        for ino_num in range(number_ino_x):
            ino = Ino(screen)
            ino.x = ino_width + 2 * (ino_width * ino_num)
            ino.y = ino_height + 1.5 * (ino_height * row_number)
            ino.rect.x = ino.x
            ino.rect.y = ino.rect.height + ino.rect.height * row_number
            inos.add(ino)


def update_inos(stats, screen, gun, inos, bullets):
    inos.update()
    if pygame.sprite.spritecollideany(gun, inos):
        gun_kill(stats, screen, gun, inos, bullets)

    inos_check(stats, screen, gun, inos, bullets)


def gun_kill(stats, screen, gun, inos, bullets):
    stats.guns_left -= 1
    inos.empty()
    bullets.empty()
    create_army(screen, inos)
    gun.create_gun()
    time.sleep(1)


def inos_check(stats, screen, gun, inos, bullets):
    screen_rect = screen.get_rect()
    for ino in inos.sprites():
        if ino.rect.bottom >= screen_rect.bottom:
            gun_kill(stats, screen, gun, inos, bullets)
            break

def check_high_score(stats, sc):
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sc.image_high_score()
        with open('highscore.txt', 'w') as f:
            f.write(str(stats.high_score))

