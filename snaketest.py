import pygame
import random
import os
import time

## Sprite size ##
SIZE = 32
pygame.init()

## Creates screen ##
screen = pygame.display.set_mode((800,600))

## Title and Icon ##
pygame.display.set_caption("Snake")
icon = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\snek.png")
pygame.display.set_icon(icon)

## Mouse image ##
#mouseimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\mouse.png")
#mouseX = random.randint (50, 750)
#mouseY = random.randint (50, 550)

## death noises ##
mouse_death1 = pygame.mixer.Sound('C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\deadscrm.wav')
mouse_death2 = pygame.mixer.Sound('C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\SamK.wav')
mouse_death1.set_volume(0.05)
mouse_death2.set_volume(0.05)

# Player image
#playerimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\player.png")
#playerX = 370
#playerY = 300
#playerX_change = 0
#playerY_change = 0
#last_direction = "up"
running = True



## MOUSE CLASS ##
class Mouse:

    def __init__(self):
        self.x = random.randint (50, 750)
        self.y = random.randint (50, 550)
        self.mouseimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\mouse.png")
        #screen.blit(self.mouseimg, (self.x,self.y))
    
    def move(self):
        self.x = random.randint (50, 750)
        self.y = random.randint (50, 550)
  
## SNAKE CLASS ##
class Snake():
    def __init__ (self):
        self.x = 370
        self.y = 300
        self.x_change = 0
        self.y_change = 0
        self.playerimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\player.png")
        self.direction = "down"
        #screen.blit(self.playerimg,(self.playerX, self.playerY))


## IMAGE ROTATION ##
    def image_rotate(self):
        
        if self.direction == "left":
            self.rotated_image = pygame.transform.rotate(self.playerimg, 270)
        if self.direction == "right":
            self.rotated_image = pygame.transform.rotate(self.playerimg, 90)
        if self.direction == "down":
            self.rotated_image = pygame.transform.rotate(self.playerimg, 0)
        if self.direction == "up":
            self.rotated_image = pygame.transform.rotate(self.playerimg, -180)

## MOVEMENT DYNAMICS ##
    def non_drift(self):
        snake.x_change = 0 
        snake.y_change = 0

    def left(self):
        self.x_change = -0.07
        self.direction = "left"
        
    def right(self):
        self.x_change = 0.07
        self.direction = "right"
        
    def down(self):
        self.y_change = 0.07
        self.direction = "down"
        
    def up(self):
        self.y_change = -0.07
        self.direction = "up"

## COLLISION ##    
def collision(x1, y1, x2, y2):
    if x1 >= x2 and x1 <= x2 + SIZE:
        if y1 >= y2 and y1 <= y2 + SIZE:
            print("yay")
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

        
            
    #Keystrokes
        #if event.type == pygame.KEYDOWN: 
            #if event.key == pygame.K_LEFT:
                #playerX_change = -0.07
                #print("left arrow is pressed")

            #if event.key == pygame.K_RIGHT:
                #print("right arrow is pressed")
                #playerX_change = 0.07
            
            #if event.key == pygame.K_UP:
                #playerY_change = -0.07
                #print("up arrow is pressed")
            #if event.key == pygame.K_DOWN:
               # playerY_change = 0.07
                #print("down arrow is pressed")

        # Player reset
        if event.type == pygame.KEYUP:
            snake.non_drift()
    
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
    #if snake.direction == "left":
        #snake.r = pygame.transform.rotate(snake.playerimg, 270)
    #if snake.direction == "right":
        #snake.r = pygame.transform.rotate(snake.playerimg, 90)
    #if snake.direction == "down":
        #snake.r = pygame.transform.rotate(snake.playerimg, 0)
    #if snake.direction == "up":
        #snake.r = pygame.transform.rotate(snake.playerimg, -180)
    
    #Direction change
    snake.y += snake.y_change
    snake.x += snake.x_change

    #Boundary stop
    if snake.y <=0:
        snake.y = 0
    
    elif snake.y >=568:
        snake.y = 568

    if snake.x <=0:
        snake.x = 0

    elif snake.x >= 768:
        snake.x = 768
    if collision(snake.x, snake.y, mouse.x, mouse.y):
        mouse.move()
        noise = random.randint(1,2)
        if noise == 1:
            mouse_death1.play()
        else:
            mouse_death2.play()
            
    screen.blit(mouse.mouseimg, (mouse.x,mouse.y))
    screen.blit(snake.rotated_image,(snake.x, snake.y))
    #Mouse(mouseX,mouseY)
    #player(playerX,playerY)
    
    pygame.display.update()