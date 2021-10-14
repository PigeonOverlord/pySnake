import pygame
import time
import random

SIZE = 32

pygame.init()

## Creates screen ##
screen = pygame.display.set_mode((800,600))

## Title and Icon ##
pygame.display.set_caption("Snake")
icon = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\snek.png")
pygame.display.set_icon(icon)

#Death noise#
mouse_death1 = pygame.mixer.Sound('C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\deadscrm.wav')
mouse_death2 = pygame.mixer.Sound('C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\SamK.wav')
mouse_death1.set_volume(0.05)
mouse_death2.set_volume(0.05)

## Mouse image ##
#mouseimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\mouse.png")

# Player image
#playerimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\player.png")

running = True



## MOUSE CLASS ##
class Mouse:

    def __init__(self):
        self.x = random.randint (50, 750)
        self.y = random.randint (50, 550)
        self.mouseimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\mouse.png")
        
    
    def move(self):
        self.x = random.randint (50, 750)
        self.y = random.randint (50, 550)
  
 ## SNAKE CLASS ##
class Snake():
    def __init__ (self):
        self.length = 3 
        self.x = [370]*self.length
        self.y = [300]*self.length
        #self.x_change = 0
        #self.y_change = 0
        self.playerimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\player.png")
        self.bodyimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\body.png")
        self.blankimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\blank.png")
        self.tailimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\tail.png")
        self.direction = "down"
        


 ## IMAGE ROTATION ##
    def image_rotate(self):

        ##following mechanic##
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]

        if self.direction == "left":
            self.x[0] -= 32
            self.rotated_image = pygame.transform.rotate(self.playerimg, 270)
            self.rotated_body = pygame.transform.rotate(self.bodyimg, 270)
        if self.direction == "right":
            self.x[0] += 32
            self.rotated_image = pygame.transform.rotate(self.playerimg, 90)
            self.rotated_body = pygame.transform.rotate(self.bodyimg, 90)
        if self.direction == "down":
            self.y[0] += 32
            self.rotated_image = pygame.transform.rotate(self.playerimg, 0)
            self.rotated_body = pygame.transform.rotate(self.bodyimg, 0)
        if self.direction == "up":
            self.y[0] -= 32
            self.rotated_image = pygame.transform.rotate(self.playerimg, -180)
            self.rotated_body = pygame.transform.rotate(self.bodyimg, -180)

 ## MOVEMENT DYNAMICS ##
    def non_drift(self):
        self.x[0] += 0 
        self.y[0] += 0

    def left(self):
        self.direction = "left"
        
    def right(self):
        self.direction = "right"
        
    def down(self):
        self.direction = "down"
        
    def up(self):
        self.direction = "up"

    def body_add(self):
        self.length += 1
        self.x.append(self.length)
        self.y.append(self.length)
        print(self.x)
        print(self.y)
        
    def draw(self):
        for i in range(self.length):
            screen.blit(self.rotated_body,(self.x[i], self.y[i]))
        screen.blit(self.blankimg,(self.x[0], self.y[0]))
        screen.blit(self.rotated_image,(self.x[0], self.y[0]))

        
def noise():
    noise = random.randint(1,2)
    if noise == 1:
        mouse_death1.play()
    else:
        mouse_death2.play()

 ## COLLISION ##    
def collision(x1, y1, x2, y2):
    if x1 >= x2 and x1 <= x2 + SIZE:
        if y1 >= y2 and y1 <= y2 + SIZE:
            #snake.length += 1
            print(snake.length)
            return True
            
    
    return False


mouse = Mouse()
snake = Snake()
# Game loop
running = True
while running:
    #Screen RGB
    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        # Player reset
        if event.type == pygame.KEYDOWN:
            #snake.non_drift()
    
            if event.key == pygame.K_LEFT:
                snake.left()
                
            if event.key == pygame.K_RIGHT:
                snake.right()
                
            if event.key == pygame.K_UP:
                snake.up()
                
            if event.key == pygame.K_DOWN:
                snake.down()

    
    #Image rotate
    snake.image_rotate()
    

    if collision(snake.x[0], snake.y[0], mouse.x, mouse.y):
            mouse.move()
            snake.body_add()
            noise()
            
    
    #Boundary stop
    if snake.y[0] <=0:
        snake.y[0] = 0
    
    elif snake.y[0] >=568:
        snake.y[0] = 568

    if snake.x[0] <=0:
        snake.x[0] = 0

    elif snake.x[0] >= 768:
        snake.x[0] = 768
    
    screen.blit(mouse.mouseimg, (mouse.x,mouse.y))

    snake.draw()
    #screen.blit(snake.rotated_image,(snake.x[0], snake.y[0]))
    #for i in range(snake.length):
        #screen.blit(snake.bodyimg,(snake.x[i:], snake.y[i:]))
    #screen.blit(snake.rotated_image,(snake.x[0], snake.y[0]))
    #screen.blit(snake.bodyimg,(snake.x-32,snake.y-32))
    #Mouse(mouseX,mouseY)
    #player(playerX,playerY)
    time.sleep(0.09)
    pygame.display.update()