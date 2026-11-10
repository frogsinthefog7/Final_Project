import pygame
import button
from time import *

pygame.init()
screen = pygame.display.set_mode((1000,500))#add ,pygame.FULLSCREEN to make it not have an x out button
pygame.display.set_caption("SweetHearts")
clock = pygame.time.Clock()
running = True

#load in assets
Bedroom_button_image_pushed = pygame.image.load("Bedroom_pushed.png").convert_alpha()
Bedroom_button_image_unpushed = pygame.image.load("Bedroom_unpushed.png").convert_alpha()
Camera_button_image_pushed = pygame.image.load("Camera_pushed.png").convert_alpha()
Camera_button_image_unpushed = pygame.image.load("Camera_unpushed.png").convert_alpha()
DressUp_button_image_pushed = pygame.image.load("Dress-up_pushed.png").convert_alpha()
DressUp_button_image_unpushed = pygame.image.load("Dress-up_unpushed.png").convert_alpha()
Music_button_image_pushed = pygame.image.load("Music_pushed.png").convert_alpha()
Music_button_image_unpushed = pygame.image.load("Music_unpushed.png").convert_alpha()

#create buttons instance
x = screen.get_width()
y = screen.get_height()

bedroom_button_pushed = button.Button((x*3/4), (y*2/16), Bedroom_button_image_pushed, (y//100))
bedroom_button_unpushed = button.Button((x*3/4), (y*2/16), Bedroom_button_image_unpushed, (y//100))
camera_button_pushed = button.Button((x*3/4), (y*6/16), Camera_button_image_pushed, (y//100))
camera_button_unpushed = button.Button((x*3/4), (y*6/16), Camera_button_image_unpushed, (y//100))
DressUp_button_pushed = button.Button((x*3/4), (y*10/16), DressUp_button_image_pushed, (y//100))
DressUp_button_unpushed = button.Button((x*3/4), (y*10/16), DressUp_button_image_unpushed, (y//100))
Music_button_pushed = button.Button((x*3/4), (y*14/16), Music_button_image_pushed, (y//100))
Music_button_unpushed = button.Button((x*3/4), (y*14/16), Music_button_image_unpushed, (y//100))
#use scale 8 for macbook

color_fill = "Pink"

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill(color_fill)

    if bedroom_button_unpushed.draw(screen) == True:
            screen.fill(color_fill)
            camera_button_unpushed.draw(screen)
            DressUp_button_unpushed.draw(screen)
            Music_button_unpushed.draw(screen)
            bedroom_button_pushed.draw(screen)
            pygame.display.flip()
            pygame.display.update()
            sleep(.5)
            if color_fill == "Pink":
                color_fill = (202,228,241)
            else:
                color_fill = "Pink"

    # RENDER YOUR GAME HERE
    if camera_button_unpushed.draw(screen) == True:
        screen.fill(color_fill)
        camera_button_pushed.draw(screen)
        DressUp_button_unpushed.draw(screen)
        Music_button_unpushed.draw(screen)
        bedroom_button_unpushed.draw(screen)
        pygame.display.flip()
        pygame.display.update()
        sleep(.5)
        if color_fill == "Pink":
            color_fill = (202,228,241)
        else:
            color_fill = "Pink"

    if DressUp_button_unpushed.draw(screen) == True:
            screen.fill(color_fill)
            DressUp_button_pushed.draw(screen)
            camera_button_unpushed.draw(screen)
            Music_button_unpushed.draw(screen)
            bedroom_button_unpushed.draw(screen)
            pygame.display.flip()
            pygame.display.update()
            sleep(.5)
            if color_fill == "Pink":
                color_fill = (202,228,241)
            else:
                color_fill = "Pink"

    if Music_button_unpushed.draw(screen) == True:
            screen.fill(color_fill)
            Music_button_pushed.draw(screen)
            camera_button_unpushed.draw(screen)
            DressUp_button_unpushed.draw(screen)
            bedroom_button_unpushed.draw(screen)
            pygame.display.flip()
            pygame.display.update()
            sleep(.5)
            if color_fill == "Pink":
                color_fill = (202,228,241)
            else:
                color_fill = "Pink"



    # flip() the display to put your work on screen
    pygame.display.flip()
    pygame.display.update()
    
    clock.tick(60)  # limits FPS to 60

pygame.quit()