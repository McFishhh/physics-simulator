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

        if self.rectFill.left < 0:
            self.velocity.x = abs(self.velocity.x)
        if self.rectFill.right > Global.SCREEN_WDITH:
            self.velocity.x = -abs(self.velocity.x)
        if self.rectFill.top < 0:
            self.velocity.y = abs(self.velocity.y)
        if self.rectFill.bottom > Global.SCREEN_HEIGHT:
            self.velocity.y = -abs(self.velocity.y)
    
    def Draw(self, screen):
        pygame.draw.rect(screen, Global.RED, self.rectFill)
        pygame.draw.rect(screen, Global.GREEN, self.rectBorder, 1)

class BlockManager:
    def __init__(self):
        self.blockList = []

        # temp
        self.blockList.append(Block(5, Vector2(Global.SCREEN_WDITH/2 - 200, Global.SCREEN_HEIGHT/2), Vector2(400, 200)))
        self.blockList.append(Block(10, Vector2(Global.SCREEN_WDITH/2 + 200, Global.SCREEN_HEIGHT/2), Vector2(-600, 200)))
        self.blockList.append(Block(15, Vector2(100, 100), Vector2(100, 100)))
    
    def __CollisionTester(self, rect1, rect2)->str:
        if rect1.rectFill.colliderect(rect2.rectFill):
            dr = abs(rect1.rectFill.right - rect2.rectFill.left)
            dl = abs(rect1.rectFill.left - rect2.rectFill.right)
            db = abs(rect1.rectFill.bottom - rect2.rectFill.top)
            dt = abs(rect1.rectFill.top - rect2.rectFill.bottom)

            if min(dl, dr) < min(dt, db):
                return 'side'
            else:
                return 'cap'
        return
    
    def __CollisionCalculate(self, rect1, rect2):
        CollisionLoc = self.__CollisionTester(rect1, rect2)

        if CollisionLoc is None:
            return

        m1 = rect1.mass
        m2 = rect2.mass

        if CollisionLoc == 'side':
            u1 = rect1.velocity.x
            u2 = rect2.velocity.x
        else:
            u1 = rect1.velocity.y
            u2 = rect1.velocity.y
        
        v1 = ((m1 - m2)/(m1 + m2)) * u1 + ((2 * m2)/(m1 + m2)) * u2
        v2 = ((2 * m1)/(m1 + m2)) * u1 + ((m2 - m1)/(m1 + m2)) * u2

        if CollisionLoc == 'side':
            rect1.velocity.x = v1
            rect2.velocity.x = v2
        else:
            rect1.velocity.y = v1
            rect2.velocity.y = v2

    def Update(self, dt):
        for block in self.blockList:
            block.Update(dt)

        n = len(self.blockList)
        for i in range(n - 1):
            rect1 = self.blockList[i]
            for j in range(i + 1, n):
                rect2 = self.blockList[j]
                self.__CollisionCalculate(rect1, rect2)

    def Draw(self, screen):
        for block in self.blockList:
            block.Draw(screen)