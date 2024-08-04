import pygame

pygame.init()


window = pygame.display.set_mode((500, 400))

while True:

    pygame.draw.line(window, (255,255,255), (0,0), (500, 400), 2)
    pygame.display.update()
