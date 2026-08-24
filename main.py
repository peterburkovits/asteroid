import pygame
import sys
from asteroidfield import AsteroidField
from asteroid import Asteroid
from player import Player
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, SHOT_RADIUS
from logger import log_event
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH} ")
    print(f"Screen height: {SCREEN_HEIGHT} ")
    
    pygame.init()
    dt = 0.0
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    asteroids = pygame.sprite.Group() # Ezek groupok lesznek
    updatable = pygame.sprite.Group() # Ezek groupok lesznek
    shots = pygame.sprite.Group() # Ezek groupok lesznek
    drawable = pygame.sprite.Group()
    AsteroidField.containers = (updatable,)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, updatable, drawable)

    asteroid_field = AsteroidField()

    Player.containers = (updatable, drawable)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return        
        screen.fill(("black"))
        updatable.update(dt)
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print(f"Game Over!")
                sys.exit(0)
        for asteroid in asteroids:
            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    asteroid.split()
                    shot.kill()
        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000  # Amount of seconds between each loop


if __name__ == "__main__":
    main()
 