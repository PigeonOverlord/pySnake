import pygame
import os
import random

pygame.init()

#Creates screen
screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Snake")
icon = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\snek.png")
pygame.display.set_icon(icon)

#Mouse image
mouseimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\mouse.png")
mouseX = random.randint (50, 750)
mouseY = random.randint (50, 550)

# Player
# Player image
playerimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\player.png")
playerX = 370
playerY = 300
playerX_change = 0
playerY_change = 0
last_direction = "up"
running = True
class Mouse:

    def __init__(self, x,y):
        screen.blit(mouseimg, (x,y))

def player(x,y):
    screen.blit(r_snake, (x, y))
    #screen.blit(playerimg(x, y))
   
#def collision(mouseX, mouseY, playerX, playerY):


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
            playerX_change = 0 
            playerY_change = 0

            if event.key == pygame.K_LEFT:
                playerX_change = -0.07
                last_direction = "left" 

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.07
                last_direction = "right"

            if event.key == pygame.K_UP:
                playerY_change = -0.07
                last_direction = "up"

            if event.key == pygame.K_DOWN:
                playerY_change = 0.07
                last_direction = "down"


    #Direction rotate
    if last_direction == "left":
        r_snake = pygame.transform.rotate(playerimg, 270)
    if last_direction == "right":
        r_snake = pygame.transform.rotate(playerimg, 90)
    if last_direction == "down":
        r_snake = pygame.transform.rotate(playerimg, 0)
    if last_direction == "up":
        r_snake = pygame.transform.rotate(playerimg, -180)
        
    #Direction change
    playerY += playerY_change
    playerX += playerX_change

    #Boundary stop
    if playerY <=0:
        playerY = 0
    
    elif playerY >=568:
        playerY = 568

    if playerX <=0:
        playerX = 0

    elif playerX >= 768:
        playerX = 768
    
    Mouse(mouseX,mouseY)
    player(playerX,playerY)
    pygame.display.update()