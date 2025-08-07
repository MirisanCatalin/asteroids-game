import sys
import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot


def main():
    pygame.init()

    score = 0
    score_font = pygame.font.SysFont("comicsans", 30)

    lives = 3
    lives_font = pygame.font.SysFont("comicsans", 30)

    game_over = False
    game_over_font = pygame.font.SysFont("comicsans", 70)

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    dt = 0

    while lives != 0:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        for asteroid in asteroids:
            if asteroid.collides_with(player):
                lives -= 1
                asteroid.kill()
                for ast in asteroids:
                    ast.kill()
                player.respawn()

                if lives == 0:
                    break

        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.collides_with(bullet):
                    bullet.kill()
                    asteroid.kill()
                    score += 10

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        score_surface = score_font.render(f"Score: {score}", True, (255, 255, 255))
        score_rect = score_surface.get_rect()
        score_rect.topleft = (10, 10)
        screen.blit(score_surface, score_rect)

        lives_surface = lives_font.render(f"Lives: {lives}", True, (255, 255, 255))
        lives_rect = lives_surface.get_rect(topright=(SCREEN_WIDTH - 10, 10))
        screen.blit(lives_surface, lives_rect)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        updatable.update(dt)

        screen.fill("black")
        game_over_surface = game_over_font.render("Game Over!", True, (255, 255, 255))
        game_over_rect = game_over_surface.get_rect(center=(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2))
        screen.blit(game_over_surface, game_over_rect)

        pygame.display.flip()

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
