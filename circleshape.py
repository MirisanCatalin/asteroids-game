import pygame
from constants import *


# Base class for game objects
class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x, y, radius):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, screen):
        # sub-classes must override
        pass

    def update(self, dt):
        # sub-classes must override
        pass

    def collides_with(self,other):
        return self.position.distance_to(other.position) <= self.radius + other.radius

    def warp_around(self,dt):
        self.position += self.velocity * dt
        if self.position.x > SCREEN_WIDTH + self.radius:
            self.position.x = 0 - self.radius
        elif self.position.x < 0 - self.radius:
            self.position.x = SCREEN_WIDTH + self.radius

            # Check for screen wrapping on the y-axis
        if self.position.y > SCREEN_HEIGHT + self.radius:
            self.position.y = 0 - self.radius
        elif self.position.y < 0 - self.radius:
            self.position.y = SCREEN_HEIGHT + self.radius