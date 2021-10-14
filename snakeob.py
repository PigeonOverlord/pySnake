import pygame
import random

#pygame.init()

#Creates screen
#screen = pygame.display.set_mode((800,600))

# Title and Icon
pygame.display.set_caption("Snake")
icon = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\snek.png")
pygame.display.set_icon(icon)

#Mouse and Snake image
#mouseimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\mouse.png")
#playerimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\player.png")

# Player start position



# Mouse class
class Mouse():
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.mouseimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\mouse.png")  
        self.x = random.randint (50, 750)
        self.y = random.randint (50, 550)
    
    def draw(self):
        self.parent_screen.blit(self.mouseimg, (self.y,self.y))

# Snake class
class Snake():
    def __init__(self,parent_screen):
        self.parent_screen = parent_screen
        self.playerimg = pygame.image.load("C:\\Users\\peter\\Desktop\\Python stuff\\Snake\\player.png")
        self.x = 370
        self.y = 300
        self.direction = "down"

    def draw(self):
        
        if self.direction == "left":
            self.playerimg = pygame.transform.rotate(self.playerimg, 270)
        if self.direction == "right":
            self.playerimg = pygame.transform.rotate(self.playerimg, 90)
        if self.direction == "down":
            self.playerimg = pygame.transform.rotate(self.playerimg, 0)
        if self.direction == "up":
            self.playerimg = pygame.transform.rotate(self.playerimg, -180)
        self.parent_screen.blit(self.playerimg, (self.y,self.y))
        pygame.display.update() 
         
       
    def left(self):

        self.x_change = -0.07
        self.x += self.x_change
        self.direction = "left"
        print(self.direction)
        self.draw()
        
    def right(self):
        
        self.x += 0.07
        self.direction = "right"
        print(self.direction)
        self.draw()
        
    def down(self):

        self.y += -0.07
        self.direction = "down"
        self.draw()
        
    def up(self):

        self.y += 0.07
        self.direction = "up"
        self.draw()
        
        
        
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800,600))
        self.snake = Snake(self.screen)
        self.snake.draw()
          
        
    def run(self):
        running = True

        while running:
           for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

        # Player movement
                if event.type == pygame.KEYUP:

                    if event.key == pygame.K_LEFT:
                        self.snake.left()
                        
                    if event.key == pygame.K_RIGHT:
                        self.snake.right()
                         
                    if event.key == pygame.K_UP:
                        self.snake.up()
                          
                    if event.key == pygame.K_DOWN:
                        self.snake.down()
        
                          

game = Game()
game.run()





    #mousey= Mouse()
    #mousey.randomize_position()
    #mousey.mouse_draw()
    #player = Snake()
    #player.snake_draw()
    #pygame.display.update()     