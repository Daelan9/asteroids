import pygame
import player
import circleshape
from constants import *

def main():
    pygame.init()
    font = pygame.font.Font(None, 36)
    fps = pygame.time.Clock()
    dt = 0
    print("Starting Asteroids!")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    black = (0, 0, 0)
    character = player.Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        dt = fps.tick(60) / 1000
        screen.fill(black)
        fps_text = font.render(f"FPS:{fps.get_fps():.2f}", True, (255, 0, 0))
        screen.blit(fps_text, (1150,10))
        character.draw(screen)
        character.update(dt)
        pygame.display.flip()

if __name__ == "__main__":    
    main()
