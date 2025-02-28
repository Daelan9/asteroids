import pygame
import player
import circleshape
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    font = pygame.font.Font(None, 36)
    fps = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0)
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)
    character = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = fps.tick(60) / 1000
        screen.fill(black)
        fps_text = font.render(f"FPS:{fps.get_fps():.2f}", True, (255, 0, 0))
        screen.blit(fps_text, (1150,10))
        updatable.update(dt)
        for drawable_object in drawable:
            drawable_object.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":    
    main()
