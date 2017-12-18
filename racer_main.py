import pygame

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
#colors are measured in RGB

car_width = 193

pygame.init()
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Racers')
clock = pygame.time.Clock()

car_img = pygame.image.load('starter_car.png')

def car(x, y):
    game_display.blit(car_img, (x, y))

def game_loop():

    x = (display_width * .4)
    y = (display_height * .75)
    #0,0 is the top left of the window. X is right, adding to y is down

    x_change = 0

    crashed = False

    exit_status = False

    while not crashed and not exit_status:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_status = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0


        x += x_change            

        game_display.fill(white)      
        car(x, y)

        if x > display_width - car_width or x < 0:
            crashed = True
        
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
