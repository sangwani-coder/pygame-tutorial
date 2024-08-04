import pygame, sys, random
import pygame.locals as GAME_GLOBALS
import pygame.event as GAME_EVENTS


pygame.init()
windowWidth = 640
windowHeight = 480
surface = pygame.display.set_mode((windowWidth, windowHeight))
pygame.display.set_caption('Pygame Shapes!')

squaresRed = random.randint(0, 255)
squaresBlue = random.randint(0, 255)
squaresGreen = random.randint(0, 255)

#chunk 05
while True:
    surface.fill((0,0,0)) # used to clear pixel data from the previous frame.
    pygame.draw.rect(
            surface,
            (squaresRed, squaresGreen, squaresBlue),
            (50, 50, windowWidth / 2, windowHeight / 2))
    if squaresRed >= 255:
        squaresRed = random.randint(0, 255)
    else:
        squaresRed += 1
    if squaresGreen >= 255:
        squaresGreen = random.randint(0, 255)
    else:
        squaresGreen += 1
    if squaresBlue >= 255:
        squaresBlue = random.randint(0,255)
    else:
        squaresBlue += 1

    # Bottom
    for event in GAME_EVENTS.get():
        if event.type == GAME_GLOBALS.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
