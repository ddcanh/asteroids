
import pygame
import random

from constants import ASTEROID_MIN_RADIUS
from circleshape import CircleShape


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)

  def draw(self, screen):
    pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
  
  def update(self, dt):
    self.position += self.velocity * dt
  
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    angle = random.uniform(0, 50)
    vector1 = self.velocity.rotate(angle)
    vector2 = self.velocity.rotate(-angle)
    new_radius = self.radius - ASTEROID_MIN_RADIUS
    asteriod1 = Asteroid(self.position.x, self.position.y, new_radius)
    asteriod1.velocity = vector1 * 1.2
    asteriod2 = Asteroid(self.position.x, self.position.y, new_radius)
    asteriod2.velocity = vector2 * 1.2
