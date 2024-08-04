import pygame

pygame.init()

window = pygame.display.set_mode((500, 400))
pygame.display.set_caption('Draw Circles')
while True:

    pygame.draw.circle(window, (255,100,0), (100,200),2, 0)
    pygame.draw.circle(window, (255,255,0), (200,200),20,1)
    pygame.draw.circle(window, (255,0,255), (300,200),20,2)
    pygame.display.update()
