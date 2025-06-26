import app
import pygame
from pygame.locals import *
from djitellopy import tello

me = tello.Tello()
me.connect()

battery = me.get_battery()

pygame.init()
screen = pygame.display.set_mode((600, 600))

def draw():
    screen.fill((0,0,0));
    #indicador bateria
    pygame.draw.rect(screen, (128,128,128), [450,40, 100, 30])
    if battery > 20:
        pygame.draw.rect(screen, (0,255,0), [450,40, battery, 30])
    else:
        pygame.draw.rect(screen, (255,0,0), [450,40, battery, 30])
    pygame.draw.rect(screen, (0,0,0), [450,40, 100, 30],2)  
    
app.run(draw)