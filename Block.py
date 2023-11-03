import Global
import pygame
from pygame.math import Vector2

class Block:
    def __init__(self, mass, position:Vector2, velocity:Vector2):
        self.mass = mass
        self.velocity = velocity
        width = mass * 10

        self.rectFill   = pygame.Rect((0, 0), (width, width))
        self.rectBorder = pygame.Rect((0, 0), (width, width))

        self.rectFill.center = position
        self.rectBorder.center = position
    
    def Update(self, dt):
        self.rectFill.move_ip(self.velocity * dt)
        self.rectBorder.move_ip(self.velocity * dt)

        if self.rectFill.left < 0 or self.rectFill.right > Global.SCREEN_WDITH:
            self.velocity.x = -self.velocity.x
        if self.rectFill.top < 0 or self.rectFill.bottom > Global.SCREEN_HEIGHT:
            self.velocity.y = -self.velocity.y
    
    def Draw(self, screen):
        pygame.draw.rect(screen, Global.RED, self.rectFill)
        pygame.draw.rect(screen, Global.GREEN, self.rectBorder, 1)

class BlockManager:
    def __init__(self):
        self.blockList = []

        # temp
        self.blockList.append(Block(5, Vector2(Global.SCREEN_WDITH/2 - 200, Global.SCREEN_HEIGHT/2), Vector2(400, 0)))
        self.blockList.append(Block(10, Vector2(Global.SCREEN_WDITH/2 + 200, Global.SCREEN_HEIGHT/2), Vector2(-600, 0)))
    
    def Update(self, dt):
        for block in self.blockList:
            block.Update(dt)
        
        n = len(self.blockList)
        for i in range(n - 1):
            first = self.blockList[i]
            for j in range(i + 1, n):
                second = self.blockList[j]

                if first.rectFill.colliderect(second.rectFill):
                    u1 = first.velocity.x
                    m1 = first.mass

                    u2 = second.velocity.x
                    m2 = second.mass

                    v1 = ((m1 - m2)/(m1 + m2)) * u1 + ((2 * m2)/(m1 + m2)) * u2
                    v2 = ((2 * m1)/(m1 + m2)) * u1 + ((m2 - m1)/(m1 + m2)) * u2

                    first.velocity.x = v1
                    second.velocity.x = v2
                    print(v1, v2)

    def Draw(self, screen):
        for block in self.blockList:
            block.Draw(screen)