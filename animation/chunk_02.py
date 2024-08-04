import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS


pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes!')


greenSquareX = windowWidth / 2
greenSquareY = windowHeight / 2
blueSquareX = 0.0
blueSquareY = 0.0

# chunk 02
while True:
    surface.fill((0,0,0))
    pygame.draw.rect(surface, (0,255,0), (greenSquareX, greenSquareY, 10, 10))
    # +X moves forward, -X moves backward
    # The bigger the number the faster the object appears to move
    greenSquareX -= 1
    # +Y moves downwards, -Y moves upwards
    #greenSquareY -= 0.5
    # The object has 8 directions with ints. use floats to achieve 360 motion
    # +X+y -> right and down
    # -X+y -> left and down
    # -X-y -> left and up
    # +X-y -> right and up
    pygame.draw.rect(surface, (0, 0, 255), (blueSquareX, blueSquareY, 10, 10))

    # Bottom
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
