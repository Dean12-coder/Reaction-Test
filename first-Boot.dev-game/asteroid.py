import random
from circleshape import CircleShape
from constants import *
import pygame
from logger import *
class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float) -> None:
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, dt: float) -> None:
        self.position += self.velocity * dt
        
    def split(self) -> None:
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # 2. Create the first new Asteroid at the current position (self.position.x, self.position.y) 
        # with the new radius, and set its velocity to vector_1 scaled up by 1.2
        asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_1.velocity = vector_1 * 1.2

        # 3. Create the second new Asteroid at the current position
        # with the new radius, and set its velocity to vector_2 scaled up by 1.2
        asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid_2.velocity = vector_2 * 1.2
