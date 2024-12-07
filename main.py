# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
import sys
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
    
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    shots = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    Shot.containers = (shots, updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    asteroid_field = AsteroidField()
    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            new_shot = player.shoot()
            if new_shot is not None:
                 shots.add(new_shot)
            
        screen.fill('black')
        
        for update in updatable:
            update.update(dt)

        for asteroid in asteroids:
            for shot in shots:
                if shot.collision_with(asteroid):
                    shot.kill()
                    asteroid.split()
            if player.collision(asteroid):
                print('Game over!')
                sys.exit()
                
        for draw in drawable:
            draw.draw(screen)


        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000
        
        
if __name__ == "__main__":
    main()

