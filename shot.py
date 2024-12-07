import pygame
from constants import *
from circleshape import CircleShape

class Shot(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, SHOT_RADIUS)
        self.velocity = pygame.Vector2(0, 0)
        self.rect = pygame.Rect(x - SHOT_RADIUS, y - SHOT_RADIUS, 2 * SHOT_RADIUS, 2 * SHOT_RADIUS)

    def collision_with(self, asteroid):
        return self.rect.colliderect(asteroid.rect)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.topleft = (self.position.x - SHOT_RADIUS, self.position.y - SHOT_RADIUS)
