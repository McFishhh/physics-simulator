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
        dt = clock.get_time() / 1000
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    if play == True:
                        play = False
                    else:
                        play = True
                if event.key == pygame.K_RIGHT and play == False:
                    blockManager.Update(dt)       
        
        if play:
            blockManager.Update(dt)
            print(dt)
         
        screen.fill(Global.BLACK)
        blockManager.Draw(screen)
        pygame.display.update()
        
        clock.tick(tickRate)

    pygame.quit()

if __name__ == '__main__':
    main()