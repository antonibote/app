import sys
import math
from PIL import Image, ImageDraw
import pygame
from pygame.locals import *

frames = 60

def deg2rad(degrees):
    return (degrees*2*math.pi)/360

def frameRate(f):
    global frames
    frames = f

def getKey(keyName):
    ans = False
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName))
    if keyInput[myKey]:
        ans = True
    return ans

def draw_filled_arc(screen, color, pos, radius, start, end):
    pil_size = radius*2
    pil_image = Image.new("RGBA", (pil_size, pil_size))
    pil_draw = ImageDraw.Draw(pil_image)

    pil_draw.pieslice((0, 0, pil_size-1, pil_size-1), start, end, fill=color)

    # - convert into PyGame image -
    mode = pil_image.mode
    size = pil_image.size
    data = pil_image.tobytes()
    image = pygame.image.fromstring(data, size, mode)
    image_rect = image.get_rect(topleft=pos)
    
    # blit image
    screen.blit(image, image_rect)
    

def run(draw):
    global frames
    
    clock = pygame.time.Clock()
    running = True
    while running:
        # Wait for fps
        clock.tick(frames)
        
        # Wait for events
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
    
        # Draw
        draw()
    
        # Blit everything
        pygame.display.flip()
    
    pygame.quit()
    sys.exit()