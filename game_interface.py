import pygame

#pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    #poll for events
    #pygame.QUIT event means user clicked X to close window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #fill screen with color to wipe away anything from last frame
    screen.fill("purple")


    #Render game here

    #flip() the display to put work on screen
    pygame.display.flip()

    #limmits fps to 60
    clock.tick(60) 

pygame.quit()