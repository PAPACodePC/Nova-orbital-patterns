import pygame, sys
import os
from datetime import datetime
from ui.buttons import Button
from utilities.get_rainbow_color import get_rainbow_color
from planets.planets import update_and_draw_planets, from_centre, planets

# Initialize variables
planets = {}
count = 0

# Initialize Pygame and set up screen display
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Orbit Visualizer")

# Get screen dimensions and set frame rate
width = screen.get_width()
height = screen.get_height()
fps = pygame.time.Clock()

counter = 0
centre = (width//2,height//2)
show_axes = False

lines = []