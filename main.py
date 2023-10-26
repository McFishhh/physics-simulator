import Global
import pygame
from pygame.locals import *

def main():
    pygame.init()
    
    screen = pygame.display.set_mode((Global.SCREEN_WDITH, Global.SCREEN_HEIGHT))
    pygame.display.set_caption('Physics simulator')
    
    clock = pygame.time.Clock()

    rectangle = pygame.Rect(60, 20, 60, 60)
    speed = [5, 10]

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        rectangle = rectangle.move(speed)

        if rectangle.left < 0 or rectangle.right > Global.SCREEN_WDITH:
            speed[0] = -speed[0]
        if rectangle.top < 0 or rectangle.bottom > Global.SCREEN_HEIGHT:
            speed[1] = -speed[1]
        
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (255, 0, 0), rectangle)
        pygame.display.update()
        dt = clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()