import pygame
import random

WIDTH, HEIGTH = 500, 500
xCells, yCells = 25, 25
xSize, ySize = WIDTH/xCells, HEIGTH/yCells

xMid, yMid = int(xCells/2), int(yCells/2)

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGTH))

COLORS = {'k':(0,0,0),'w':(255,255,255),'g':(0,255,0),'r':(255,0,0)}


class Snake(self):
    self.body = []
    self.length = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def add(self,Square):
        self.body.append(Square(x,y))
        self.length += 1
    def plot(self):
        for i in range(0,self.length):
            iBody = self.body[i]
            poly = [(iBody.x*xSize,iBody.y*ySize),
                ((iBody.x+1)*xSize,iBody.y*ySize),
                ((iBody.x+1)*xSize,(iBody.y+1)*ySize),
                (iBody.x*xSize,(iBody.y+1)*ySize)]
            pygame.draw.polygon(screen,COLORS['g'],poly,1)
        
class Square(self):
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
class Food(self):
    self.x = random.randint(0,xCells)
    self.y = random.randint(0,yCells)
    def __init__(self):
        pass
    def plot(self):
        poly = [(self.x*xSize,self.y*ySize),
                ((self.x+1)*xSize,self.y*ySize),
                ((self.x+1)*xSize,(self.y+1)*ySize),
                (self.x*xSize,(self.y+1)*ySize)]
        pygame.draw.polygon(screen,COLORS['r'],poly,1)
        
snake = Snake(xMid,yMid)
snake.add(Square(xMid,yMid))

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.x += -1
                snake.y += 0
            if event.key == pygame.K_RIGHT:
                snake.x += 1
                snake.y += 0
            if event.key == pygame.K_UP:
                snake.x += 0
                snake.y += 1
            if event.key == pygame.K_DOWN:
                snake.x += 0
                snake.y += -1
            
    screen.fill(COLORS['k'])
    
    pygame.display.update()
    
    clock.tick(30)


pygame.quit()