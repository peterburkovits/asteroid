import pygame
from asteroid import Asteroid
from player import Player
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} ")
    print(f"Screen height: {SCREEN_HEIGHT} ")

    asteroids = pygame.sprite.Group() # Ezek groupok lesznek
    Asteroid.containers = (asteroids, updatable, drawable)
    
    pygame.init()
    dt = 0.0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group() # Ezek groupok lesznek
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        screen.fill(("black"))
        updatable.update(dt)
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop


if __name__ == "__main__":
    main()
 