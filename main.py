import pygame
import sys
import player
import asteroid
import asteroidfield
import shot
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
    shots = pygame.sprite.Group()

    asteroid.Asteroid.containers = (asteroids, updatable, drawable)
    asteroidfield.AsteroidField.containers = updatable
    player.Player.containers = (updatable, drawable)
    shot.Shot.containers = (shots, drawable)

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

        #Shooting
        for bullet in shots:
            bullet.update(dt)

        #Initiate asteroids
        for ast_obj in asteroids:

            for bullet in shots:
                if ast_obj.collision(bullet):
                    ast_obj.split()
                    bullet.kill()

            if isinstance(ast_obj, CircleShape):
                if ast_obj.collision(character):
                    print(f"Collision with an asteroid detected at {ast_obj.position}")
                    sys.exit("Game Over!")

        #Draw FPS counter
        font = pygame.font.Font(None, 36)
        fps_text = font.render(f"FPS:{fps.get_fps():.2f}", True, (255, 0, 0))
        screen.blit(fps_text, (1150,10))

        #Flip display
        pygame.display.flip()

if __name__ == "__main__":    
    main()
