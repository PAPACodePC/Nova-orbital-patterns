# main.py
import pygame
import math
import sys
import os
from datetime import datetime
from pygame.locals import *
from ui.buttons import Button
from utilities.get_rainbow_color import get_rainbow_color
from planets.planets import update_and_draw_planets, from_centre, planets

# Initialize Pygame and set up the screen
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("Orbit Visualizer")

# Screen dimensions and frame rate setup
width, height = screen.get_width(), screen.get_height()
fps = pygame.time.Clock()

# Initialize variables
centre = (width // 2, height // 2)
show_axes = False
lines = []
counter = 0
count = 0

# Define buttons
button_s = Button(10, 10, 100, 30, "Save (S)", 20, (0, 0, 255), (0, 255, 0))
button_q = Button(10, 50, 100, 30, "Quit (Q)", 20, (0, 0, 255), (0, 255, 0))
button_a = Button(10, 90, 100, 30, "Axes (A)", 20, (0, 0, 255), (0, 255, 0))
button_r = Button(10, 130, 100, 30, "Reset (R)", 20, (0, 0, 255), (0, 255, 0))
buttons = [button_s, button_q, button_a, button_r]


# Function to calculate the position from the center
def from_centre(x,y):
    return (centre[0]+x,centre[1]-y)

# Function to render the visualizer, planets, and lines
def render():
    screen.fill((0, 0, 0))
    update_and_draw_planets(screen, counter, centre, lines)
    
    # Draw planets and their orbits
    for planet in planets.values():
        planet["angle"] = planet["angle"] + planet["omega"]
        planet["x"] = planet["a"] * math.cos(planet["angle"]) # New x
        planet["y"] = planet["a"] * math.sin(planet["angle"]) # New y
        pygame.draw.circle(
            screen,
            (5, 255, 230),
            center=from_centre(planet["x"],planet["y"]),
            radius=5,
            width=1
        )
        pygame.draw.circle(
            screen,
            (0, 79, 71),
            center=centre,
            radius=planet["a"],
            width=1
        )

    # Draw lines between planets
    if count > 1:
        for i in range(1,count):
            color = get_rainbow_color(counter)
            pygame.draw.line(
                screen,
                color,
                from_centre(planets[f"{i}"]["x"], planets[f"{i}"]["y"]),
                from_centre(planets[f"{i+1}"]["x"], planets[f"{i+1}"]["y"])
            )

        for k in range(1,count):
            if counter % 6 == 0:
                color = get_rainbow_color(counter)
                lines.append(
                    (from_centre(planets[f"{k}"]["x"], planets[f"{k}"]["y"]),
                     from_centre(planets[f"{k+1}"]["x"], planets[f"{k+1}"]["y"]),
                     color)
                )

    # Draw previously stored lines
    for j in lines:
        pygame.draw.line(screen, j[2], j[0], j[1])

    # Draw axes and circles around mouse pointer
    if show_axes == True:
        pygame.draw.line(
            screen,
            (0,255,0),
            (0, height//2),
            (width, height//2)
        )
        pygame.draw.line(
            screen,
            (0,255,0),
            (width//2, 0),
            (width//2, height)
        )
        pygame.draw.line(
            screen,
            (255,0,0),
            centre,
            pygame.mouse.get_pos()
        )

    pygame.draw.circle(
        screen,
        (0, 255, 0),     # Color (RGB): Green
        center=centre,   # Position: Center of the screen
        radius=25,       # Radius: 40 pixels
        width=40          # Width: 0 pixels (this creates a solid filled circle)
    )
    pygame.draw.circle(
        screen,
        (5, 255, 230),
        center=pygame.mouse.get_pos(),
        radius=5,
        width=25
    )
    pygame.draw.circle(
        screen,
        (0, 79, 71),
        center=centre,
        radius=math.sqrt((centre[0]-pygame.mouse.get_pos()[0])**2 + (centre[1]-pygame.mouse.get_pos()[1])**2),
        width=1
    )
    
    # Display the radius and angle at the mouse pointer
    font = pygame.font.SysFont("monospace", 15)
    radius_display = font.render(f"Radius: {round(math.sqrt((centre[0]-pygame.mouse.get_pos()[0])**2 + (centre[1]-pygame.mouse.get_pos()[1])**2))}", 1, (255,255,255))
    mouse_pos = pygame.mouse.get_pos()
    ang = math.atan2(
        centre[1]-mouse_pos[1], mouse_pos[0]-centre[0]
    )
    angledisplay = font.render(f"Angle: {round(math.degrees(ang))}", 1, (255,255,255))
    screen.blit(radius_display, mouse_pos)
    screen.blit(angledisplay, (mouse_pos[0], mouse_pos[1]+20))

    # Draw buttons
    for button in buttons:
        button.render(screen)

# Main loop to handle events and update the screen
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_q):
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if not os.path.isdir("images"):
                    os.makedirs("images")
                pygame.image.save(screen, f"images/{datetime.now().strftime('%Y-%m-%d-%H-%M-%S')}.png")
            if event.key == pygame.K_a:
                show_axes = not show_axes

        # Handle mouse events for buttons and planets
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_pos = pygame.mouse.get_pos()

            if button_s.is_mouse_over(mouse_pos):
                # Save screenshot
                pass
            elif button_q.is_mouse_over(mouse_pos):
                # Quit the application
                pygame.quit()
                sys.exit()
            elif button_a.is_mouse_over(mouse_pos):
                # Toggle axes
                show_axes = not show_axes
            elif button_r.is_mouse_over(mouse_pos):  # New reset functionality
                # Reset the visualizer
                planets = {}
                count = 0
                lines = []
            else:
                count += 1
                rad = math.sqrt((centre[0]-mouse_pos[0])**2 + (centre[1]-mouse_pos[1])**2)
                ang_vel = math.sqrt(1/rad**3)*90
                ang = math.atan2(centre[1]-mouse_pos[1], mouse_pos[0]-centre[0])
                planets[str(count)] = {
                    "a":rad,
                    "angle":ang,
                    "omega":ang_vel,
                    "x":pygame.mouse.get_pos()[0],
                    "y":pygame.mouse.get_pos()[1],
                }

    # Update button states
    mouse_pos = pygame.mouse.get_pos()
    for button in buttons:
        button.active = button.is_mouse_over(mouse_pos)

    render()
    pygame.display.update()
    fps.tick(60)