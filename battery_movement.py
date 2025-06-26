from djitellopy import tello
import pygame
import app
from pygame.locals import *
import time

me = tello.Tello()
me.connect()
me.streamon()

# Get battery
battery = me.get_battery()

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((600, 600))

# Flag to prevent re-running movement
movement_started = False

# Store key press events
pressed_keys = set()

def draw():
    global movement_started

    screen.fill((0, 0, 0))

    # Battery indicator
    pygame.draw.rect(screen, (128, 128, 128), [40, 20, 200, 30])
    if battery > 20:
        pygame.draw.rect(screen, (0, 255, 0), [40, 20, battery * 2, 30])
    else:
        pygame.draw.rect(screen, (255, 0, 0), [40, 20, battery * 2, 30])
    pygame.draw.rect(screen, (0, 0, 0), [40, 20, 200, 30], 2)

    # Check for spacebar to start movement
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_SPACE and not movement_started:
                movement_started = True
                automated_movement()

def automated_movement():
    print("Starting automated movement...")
    me.takeoff()
    time.sleep(2)

    me.move_up(50)
    time.sleep(2)

    me.rotate_clockwise(90)
    time.sleep(2)

    me.move_forward(100)
    time.sleep(2)

    me.land()
    print("Movement complete.")

# Run app loop
app.run(draw)
