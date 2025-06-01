import pygame, sys
from pygame.locals import *

BLACK = ( 0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = ( 255, 0, 0)

pygame.init()
pygame.font.init()
size = (700, 500)
screen = pygame.display.set_mode(size)
myfont = pygame.font.SysFont(None,40)
text_surface = myfont.render("Helloworld",False,(0,0,255))
text_rect = text_surface.get_rect(midtop=(100,100))
DISPLAYSURF = pygame.display.set_mode((400, 300))
pygame.display.set_caption('P.Earth')
clock = pygame.time.Clock()

running = True
while running: 
    for event in pygame.event.get():
        if event.type == QUIT:           
            pygame.quit()
            
    mouseX,mouseY = pygame.mouse.get_pos()       
    screen.fill((0,0,0))
    screen.blit(text_surface,text_rect)
    pygame.draw.rect(screen, (255, 0, 0), text_rect, 2)
    pygame.display.update() 
    clock.tick(60)



pygame.quit()