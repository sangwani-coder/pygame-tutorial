import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))

while True:

    pygame.draw.ellipse(window, (255,0,0), (100,100,100, 50))
    pygame.draw.ellipse(window, (0,255,0), (100,150,80,40))
    pygame.draw.ellipse(window, (0,0,255), (100,190,60,30))
    pygame.display.update()
