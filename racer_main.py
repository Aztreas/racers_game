import pygame
import time
import random

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)  #call Sprite initializer
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

display_width = 800
display_height = 600
high_score = 0

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 122, 66)
blue = (0, 0, 255)
#colors are measured in RGB

car_width = 130

background_road = Background('Road.png', [210,0])

pygame.init()
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Racers')
clock = pygame.time.Clock()

car_img = pygame.image.load('starter_car.png')

def obstacles(obx, oby, obw, obh, color):
    pygame.draw.rect(game_display, color, [obx, oby, obw, obh])
    

def crash(end_score):
    global high_score
    if end_score > high_score:
        high_score = end_score
    message_display('You crashed! High score: ' + str(high_score))

def message_display(string):
    font = pygame.font.Font('freesansbold.ttf', 45)
    text_surface, text_box = text_objects(string, font, red)
    text_box.center = (display_width/2, display_height/2)
    game_display.blit(text_surface, text_box)
    pygame.display.update()
    time.sleep(2)

    game_loop()
    #restarts game

def text_objects(string, font, color):
    text_surface = font.render(string, True, color)
    return text_surface, text_surface.get_rect()
    
    

def car(x, y):
    game_display.blit(car_img, (x, y))

def game_loop():

    score = 0

    x = (display_width * .4)
    y = (display_height * .75)
    #0,0 is the top left of the window. X is right, adding to y is down

    x_change = 0

    obx = random.randrange(0, display_width)
    oby = -800
    ob_speed = 8
    obw = 100
    obh = 100

    exit_status = False

    while not exit_status:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_status = True
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change
        score += 1

        game_display.fill(green)
        game_display.blit(background_road.image, background_road.rect)

        obstacles(obx, oby, obw, obh, white)
        oby += ob_speed
        car(x, y)

        if x > display_width - car_width or x < 0:
            crash()
        if oby > display_height:
            oby = 0 - obh
            obx = random.randrange(0, display_width)

        if y + 32 < oby + obh:
            if x + 70 > obx and x + 70 < obx + obw or x + car_width > obx and x + car_width < obx + obw:
                crash(score)
        
        pygame.display.update()
        #could also use pygame.display.flip, which updates the whole surface
        #update only updates its parameters

        clock.tick(60)
        #input here is the fps

game_loop()
pygame.quit()
#quits game
quit()
#quits py file and window
