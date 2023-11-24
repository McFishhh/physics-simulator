import Global
import Menu
import pygame

def main():

    pygame.init()
    
    screen = pygame.display.set_mode((Global.SCREEN_WDITH, Global.SCREEN_HEIGHT))
    pygame.display.set_caption('Physics simulator')

    menu = Menu.Menu()

    running = True
    while running: 
        running = menu.Detector()
        menu.Update()
        menu.Draw(screen)

    pygame.quit()

if __name__ == '__main__':
    main()