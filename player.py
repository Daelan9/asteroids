import pygame
import constants
import shot
from main import *
from circleshape import CircleShape

class Player(CircleShape):

    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)
    
    def rotate(self, dt):
        self.rotation += constants.PLAYER_TURN_SPEED * dt
        self.rotation %= 360

    def shoot(self):
        velocity = pygame.Vector2 (0,1)
        velocity = velocity.rotate(self.rotation)
        velocity *= constants.PLAYER_SHOOT_SPEED
        shot.Shot(self.position.x, self.position.y, velocity)
        

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)

        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_s]:
            self.move(-dt)

        if keys[pygame.K_w]:
            self.move(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * constants.PLAYER_MOVE_SPEED * dt