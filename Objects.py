import Global
import pygame
from pygame.math import Vector2

class Object:
    def __init__(self, position: Vector2, velocity: Vector2, acceleration: Vector2):
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration

class Block(Object):
    def __init__(self, mass, position: Vector2, velocity: Vector2 = Vector2(0, 0), acceleration: Vector2 = Vector2(0, 0)):
        super().__init__(position, velocity, acceleration + Global.GRAVITY)
        self.mass = mass
        
        width = mass * 10
        self.rectFill   = pygame.Rect((0, 0), (width, width))
        self.rectBorder = pygame.Rect((0, 0), (width, width))

        self.rectFill.center = position
        self.rectBorder.center = position
    
    def ChangeMass(self, mass):
        self.mass = mass
        width = mass * 10
        self.rectFill.size = (width, width)
        self.rectBorder.size = (width, width)

    def __CheckWallCollision(self):
        if self.rectFill.left < 0:
            self.velocity.x = abs(self.velocity.x)
        if self.rectFill.right > Global.SCREEN_WDITH:
            self.velocity.x = -abs(self.velocity.x)
        if self.rectFill.top < 0:
            self.velocity.y = abs(self.velocity.y)
        if self.rectFill.bottom > Global.SCREEN_HEIGHT:
            self.velocity.y = -abs(self.velocity.y)
            # self.rectFill.centery = 1000-50
            # self.rectBorder.centery = 1000-50

    def Update(self, dt):
        self.position += self.velocity * dt + 0.5 * self.acceleration * dt * dt
        self.velocity += self.acceleration * dt

        self.rectFill.center = self.position
        self.rectBorder.center = self.position

        self.__CheckWallCollision()

    def Draw(self, screen):
        pygame.draw.rect(screen, Global.RED, self.rectFill)
        pygame.draw.rect(screen, Global.GREEN, self.rectBorder, 1)
    
class BlockManager:
    def __init__(self):
        self.blockList = []
    
    def AddBlock(self):
        self.blockList.append(Block(10, Vector2(500, 500), Vector2(0, 0))) # temp
    
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
    
    def __CollisionCalculate(self):
        n = len(self.blockList)
        
        if n == 0 or n == 1:
            return

        for i in range(n - 1):
            rect1 = self.blockList[i]
            for j in range(i + 1, n):
                rect2 = self.blockList[j]

                CollisionLoc = self.__CollisionTester(rect1, rect2)

                if CollisionLoc is None:
                    continue

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

        self.__CollisionCalculate()

    def Draw(self, screen):
        for block in self.blockList:
            block.Draw(screen)