import Global
from Block import BlockManager
import pygame
from pygame.locals import *
from pygame.math import Vector2

def main():

    pygame.init()
    
    screen = pygame.display.set_mode((Global.SCREEN_WDITH, Global.SCREEN_HEIGHT))
    pygame.display.set_caption('Physics simulator')
    
    clock = pygame.time.Clock()

    blockManager = BlockManager()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        dt = clock.get_time() / 1000
    
        blockManager.Update(dt)
        
        screen.fill(Global.BLACK)
        blockManager.Draw(screen)
        pygame.display.update()
        
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()