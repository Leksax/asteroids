from circleshape import *
from constants import *
import random




class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (self.position.x, self.position.y), self.radius, width=2)    

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            new_vector1 = self.velocity.rotate(random_angle)
            new_vector2 = self.velocity.rotate(random_angle * -1)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            new_asterroid1 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asterroid2 = Asteroid(self.position.x, self.position.y, new_radius)
            new_asterroid1.velocity = new_vector1 * 1.2 
            new_asterroid2.velocity = new_vector2 * 1.2