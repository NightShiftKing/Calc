import pygame
import cartisonGraph


pygame.init()




screen = pygame.display.set_mode((700,700), pygame.RESIZABLE)
pygame.display.set_caption('Calculus demonstration')


gameover = False
clock = pygame.time.Clock()


cordPlane = cartisonGraph.Coords()


while not gameover:
    ticks = clock.get_time()
    clock.tick(60)  # FPS
    gameEvents = pygame.event.get()
    # Input Section------------------------------------------------------------
    for event in gameEvents:  # quit game if x is pressed in top corner
        if event.type == pygame.QUIT:
            gameover = True

        if event.type == pygame.MOUSEWHEEL:
            print(cordPlane.increments)
            cordPlane.increments += event.y


            
    #keyboard input-----------------------------------


    cordPlane.update()
    #render section-----------------------------------vis
    screen.fill((150,150,150))

    cordPlane.draw(screen) 



    pygame.display.flip() #update graphics each game loop

#END GAME LOOP#######################################################
pygame.quit()