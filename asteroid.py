import pygame

from circleshape import CircleShape
from constants import *
import random
import math

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)
        self.points = []
        num_points = 24
        for i in range(num_points):
            angle = (i / num_points) * (math.pi * 2)

            # Vary the radius for each point to make it lumpy
            random_radius = random.uniform(self.radius * 0.7, self.radius * 1.3)

            # Calculate the x and y coordinates for the point
            x = math.cos(angle) * random_radius
            y = math.sin(angle) * random_radius

            self.points.append(pygame.Vector2(x, y))

    def draw(self, screen):
        polygon_points = [self.position + p for p in self.points]
        pygame.draw.polygon(screen, "white", polygon_points, 2)

    def update(self, dt):
        self.position += self.velocity * dt
        self.warp_around(dt)


    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)

            new_velocity1 = self.velocity.rotate(random_angle)
            new_velocity2 = self.velocity.rotate(-random_angle)

            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = new_velocity1 * 1.2
            asteroid = Asteroid(self.position.x, self.position.y, new_radius)
            asteroid.velocity = new_velocity2 * 1.2