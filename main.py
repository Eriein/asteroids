import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from logger import log_state
from player import Player
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
    Player.containers = (updatable, drawable)
    
    player = Player(x, y)
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
        

if __name__ == "__main__":
    main()
