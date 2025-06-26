from djitellopy import tello
import pygame
import app
from pygame.locals import *

me = tello.Tello()
me.connect()
me.streamon()

# Get battery
battery = me.get_battery()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))  # Adjusted resolution for camera feed

def draw():
    screen.fill((0, 0, 0))
    
    # Draw battery indicator
    pygame.draw.rect(screen, (128, 128, 128), [40, 20, 200, 30])
    if battery > 20:
        pygame.draw.rect(screen, (0, 255, 0), [40, 20, battery * 2, 30])
    else:
        pygame.draw.rect(screen, (255, 0, 0), [40, 20, battery * 2, 30])
    pygame.draw.rect(screen, (0, 0, 0), [40, 20, 200, 30], 2)

# Run app loop with draw function
app.run(draw)