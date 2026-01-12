from constants import PLAYER_RADIUS, LINE_WIDTH, PLAYER_TURN_SPEED, PLAYER_SPEED, PLAYER_SHOOT_SPEED, PLAYER_SHOOT_COOLDOWN_SECONDS
import pygame
from circleshape import CircleShape
from shot import Shot

class Player(CircleShape):
    def __init__(self, x, y, shot_cooldown_timer):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = 0
        self.shot_cooldown_timer = 0
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.polygon(screen, "white", self.triangle(), LINE_WIDTH)

    def rotate(self, delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time):
        keys = pygame.key.get_pressed()
        self.shot_cooldown_timer -= delta_time
        if keys[pygame.K_a]:
            self.rotate(-delta_time) # rotate left
        if keys[pygame.K_d]:
            self.rotate(delta_time) # rotate right
        if keys[pygame.K_w]:
            self.move(delta_time) # forward
        if keys[pygame.K_s]:
            self.move(-delta_time) # backward
        if keys[pygame.K_SPACE]: # shoot when pressed
            self.shoot()
    
    def move(self, delta_time):
        unit_vector = pygame.Vector2(0, 1)
        rotated_vector = unit_vector.rotate(self.rotation)
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * delta_time
        self.position += rotated_with_speed_vector

    def shoot(self):
        if self.shot_cooldown_timer > 0:
            return
        else:
            self.shot_cooldown_timer = PLAYER_SHOOT_COOLDOWN_SECONDS
        shot = Shot(self.position.x, self.position.y, self.radius)
        start_vector = pygame.Vector2(0, 1)
        shot.velocity = start_vector.rotate(self.rotation) * PLAYER_SHOOT_SPEED
        


