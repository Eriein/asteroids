import pygame
import sys
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state, log_event
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot
import circleshape

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    delta_time = 0
    
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()
    player = Player(x, y, 0)
    
    # game loop
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for draw in drawable:
            draw.draw(screen)
        pygame.display.flip()
        delta_time = clock.tick(60) / 1000
        updatable.update(delta_time)
        for random_asteroid in asteroids:
            if random_asteroid.collides_with(player):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
            for shot in shots:
                if random_asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    random_asteroid.kill()
                    shot.kill()
            
        

if __name__ == "__main__":
    main()
