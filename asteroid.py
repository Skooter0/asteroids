import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rect = pygame.Rect(x - radius, y - radius, 2 * radius, 2 * radius)

    def draw(self, screen):
        pygame.draw.circle(screen, 'white', self.position, self.radius, 2)

    def collision_with(self, shot):
        return self.rect.colliderect(shot.rect)

    def split(self):
        self.kill()
        
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        new_vector1 = self.velocity.rotate(angle) * 1.2
        new_vector2 = self.velocity.rotate(-angle) * 1.2
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid1.velocity = new_vector1
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2.velocity = new_vector2

        for group in self.groups():
            group.add(asteroid1, asteroid2)
        

    def update(self, dt):
        self.position += self.velocity * dt
        self.rect.topleft = (self.position.x - self.radius, self.position.y - self.radius)
