import pygame
import random

WIDTH, HEIGTH = 750, 750
xCells, yCells = 50, 50
xSize, ySize = WIDTH/xCells, HEIGTH/yCells

xMid, yMid = int(xCells/2), int(yCells/2)

pygame.init()

clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH,HEIGTH))

pygame.display.set_caption('PySnake')

COLORS = {'k':(0,0,0),'w':(255,255,255),'g':(0,255,0),'r':(255,0,0)}

class Snake():
    def __init__(self,xIni,yIni):
        self.body = []
        self.length = 0
        self.xIni = xIni
        self.yIni = yIni
        self.x = 0
        self.y = 0
        
    def add(self):
        if self.length == 0:
            x = self.xIni
            y = self.yIni
        else:
            x = self.body[-1].x - self.x
            y = self.body[-1].y - self.y   
        self.body.append(Square(x,y))
        self.length += 1
        
    def plot(self):
        for i in range(0,self.length):
            poly = [(self.body[i].x*xSize,self.body[i].y*ySize),
                ((self.body[i].x+1)*xSize,self.body[i].y*ySize),
                ((self.body[i].x+1)*xSize,(self.body[i].y+1)*ySize),
                (self.body[i].x*xSize,(self.body[i].y+1)*ySize)]
            pygame.draw.polygon(screen,COLORS['g'],poly,0)
            
    def update(self):
        oldx1 = self.body[0].x
        oldy1 = self.body[0].y
        self.body[0].x += self.x
        self.body[0].y += self.y
        for i in range(1,self.length):
            oldx2 = self.body[i].x
            oldy2 = self.body[i].y
            self.body[i].x = oldx1
            self.body[i].y = oldy1
            oldx1 = oldx2
            oldy1 = oldy2
            
    def collision(self):
        x = self.body[0].x
        y = self.body[0].y
        for i in range(1,self.length):
            if self.body[i].x == x and self.body[i].y == y:
                return True
        return False
    
class Square():
    def __init__(self,x,y):
        self.x = x
        self.y = y
              
class Food():
    def __init__(self):
        self.x = random.randint(0,xCells-1)
        self.y = random.randint(0,yCells-1)
        
    def plot(self):
        poly = [(self.x*xSize,self.y*ySize),
                ((self.x+1)*xSize,self.y*ySize),
                ((self.x+1)*xSize,(self.y+1)*ySize),
                (self.x*xSize,(self.y+1)*ySize)]
        pygame.draw.polygon(screen,COLORS['r'],poly,0)
        
# Initialize some objects      
snake = Snake(xMid,yMid)
snake.add()
food = Food()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                snake.x = -1
                snake.y = 0
            if event.key == pygame.K_RIGHT:
                snake.x = 1
                snake.y = 0
            if event.key == pygame.K_UP:
                snake.x = 0
                snake.y = -1
            if event.key == pygame.K_DOWN:
                snake.x = 0
                snake.y = 1
            
    screen.fill(COLORS['k'])
    # Check for food collision
    head = snake.body[0]
    if head.x == food.x and head.y == food.y:
        food = Food()
        snake.add()
    if head.x < 0 or head.x > xCells or head.y < 0 or head.y > yCells:
        running = False        
    # Check snake collision
    if snake.collision():
        running = False
    # Update Position of snake
    snake.update()
    # Plot elements
    snake.plot()
    food.plot()
    
    pygame.display.update()
    
    clock.tick(30)


pygame.quit()