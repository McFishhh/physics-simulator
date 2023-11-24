import Global
import pygame
from enum import Enum
import Objects

class State(Enum):
    PLAY = 1
    PAUSE = 2
    INVENTORY = 3

class Menu:
    def __init__(self):
        self.frameRate = 60
        self.state = State.PAUSE
        self.clock = pygame.time.Clock()
        self.dt = None

        self.blockManager = Objects.BlockManager()

    def __KeyPressedDetector(self, key):
        if key == pygame.K_SPACE:
            self.state = State.PAUSE if self.state == State.PLAY else State.PLAY
        elif key == pygame.K_i:
            self.state = State.INVENTORY
            self.blockManager.AddBlock()
            self.state = State.PLAY
    
    def __KeyHoldDetector(self):
        keys = pygame.key.get_pressed()

        if self.state == State.PAUSE:
            if keys[pygame.K_RIGHT]:
                self.blockManager.Update(self.dt)

    def Detector(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            if event.type == pygame.KEYDOWN:
                self.__KeyPressedDetector(event.key)
        self.__KeyHoldDetector()

        return True

    def Update(self):
        self.dt = self.clock.get_time() / 1000  # get seconds since last frame

        if self.state == State.PLAY:
            self.blockManager.Update(self.dt)
        if self.state == State.PAUSE:
            pass

    def Draw(self, screen):
        screen.fill(Global.BLACK)
        self.blockManager.Draw(screen)
        pygame.display.update()

        self.clock.tick(self.frameRate)
