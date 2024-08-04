import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))

while True:

    pygame.draw.lines(window, (255, 255, 255),True,((50,50), (75, 75),(25,75)),1)
    pygame.draw.lines(window, (255, 255, 255),False,((100,100), (150, 150),(50,150)),1)

    pygame.display.update()
