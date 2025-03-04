import pygame
import sys
import player
import asteroid
import asteroidfield
from constants import *
from circleshape import CircleShape

def main():
    pygame.init()
    print("Starting Asteroids!")
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable
    player.Player.containers = (updatable, drawable)

    asteroid_field = asteroidfield.AsteroidField()
    character = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    #Game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        #Update game state
        dt = fps.tick(60) / 1000
        updatable.update(dt)

        #Clear screen
        screen.fill("black")

        #Draw everything
        for drawable_object in drawable:
            drawable_object.draw(screen)

        #Initiate asteroids
        for updatable_object in updatable:
            if updatable_object is character:
                continue
            if isinstance(updatable_object, CircleShape):
                if updatable_object.collision(character):
                    print(f"Collision detected at {updatable_object.position}")
                    sys.exit("Game Over!")

        #Draw FPS counter
        font = pygame.font.Font(None, 36)
        fps_text = font.render(f"FPS:{fps.get_fps():.2f}", True, (255, 0, 0))
        screen.blit(fps_text, (1150,10))

        #Flip display
        pygame.display.flip()

if __name__ == "__main__":    
    main()
