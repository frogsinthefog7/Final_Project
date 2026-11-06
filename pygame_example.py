import pygame
import button
from time import *

pygame.init()
screen = pygame.display.set_mode((0,0))#add ,pygame.FULLSCREEN to make it not have an x out button
pygame.display.set_caption("SweetHearts")
clock = pygame.time.Clock()
running = True

#load in assets
button_image = pygame.image.load("button.png").convert_alpha()

#button class


#create button instance
x = screen.get_width()
y = screen.get_height()
button = button.Button((x/2), (y/2), button_image, .5)

color_fill = "Pink"

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color_fill)

    # RENDER YOUR GAME HERE
    if button.draw(screen) == True:
        print('Button')
        if color_fill == "Pink":
            color_fill = (202,228,241)
        else:
            color_fill = "Pink"
    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()
    
    clock.tick(60)  # limits FPS to 60

pygame.quit()