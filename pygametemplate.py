#Pygame template - skeleton for a new pygame project
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30

RED     = ( 255,   0,   0)
GREEN   = (   0, 255,   0)
BLUE    = (   0,   0, 255)
WHITE   = ( 255, 255, 255)
BLACK   = (   0,   0,   0)
ORANGE  = (   0,   0,   0)


#Initialize pygame and create window
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jakobs spil")
clock = pygame.time.Clock()

#Game loop

running = True

while running:
    # Process input (events)
    # Update
    # Draw / render
    screen.fill()