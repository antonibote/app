import app
import pygame
import cv2
from pygame.locals import *
from djitellopy import tello

# Initialize Tello
me = tello.Tello()
me.connect()
me.streamon()

# Get battery
battery = me.get_battery()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((960, 720))  # Adjusted resolution for camera feed

# Define function to convert OpenCV frame to Pygame surface
def frame_to_surface(frame):
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)  # Convert to RGB
    frame = cv2.resize(frame, (960, 720))  # Resize to fit in window
    return pygame.surfarray.make_surface(frame.swapaxes(0, 1))

def draw():
    screen.fill((0, 0, 0))

    # Get frame from Tello
    frame = me.get_frame_read().frame
    surface = frame_to_surface(frame)
    screen.blit(surface, (10, 10))

    # Draw battery indicator
    pygame.draw.rect(screen, (128, 128, 128), [700, 20, 200, 30])
    if battery > 20:
        pygame.draw.rect(screen, (0, 255, 0), [700, 20, battery * 2, 30])
    else:
        pygame.draw.rect(screen, (255, 0, 0), [700, 20, battery * 2, 30])
    pygame.draw.rect(screen, (0, 0, 0), [700, 20, 200, 30], 2)

# Run app loop with draw function
app.run(draw)
