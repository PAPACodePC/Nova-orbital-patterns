# planets.py
import pygame
import math

# Initialize variables
planets = {}
count = 0

# Function to calculate the position from the center
def from_centre(x, y, centre):
    return (centre[0] + x, centre[1] - y)
# Assuming planets and count are defined at the module level as shown

def update_and_draw_planets(screen, counter, centre, lines):
    global planets, count  # Use global if these variables are defined outside the function
    for planet_id, planet in planets.items():
        planet["angle"] += planet["omega"]
        planet["x"] = planet["a"] * math.cos(planet["angle"])
        planet["y"] = planet["a"] * math.sin(planet["angle"])
        
        # Drawing the planet
        pygame.draw.circle(screen, (255, 255, 255), from_centre(planet["x"], planet["y"], centre), 5)
        
        # Drawing the orbit
        pygame.draw.circle(screen, (100, 100, 100), centre, planet["a"], 1)

    # Drawing lines between planets
    if count > 1:
        for i in range(1, count):
            if str(i) in planets and str(i+1) in planets:
                start_pos = from_centre(planets[str(i)]["x"], planets[str(i)]["y"], centre)
                end_pos = from_centre(planets[str(i+1)]["x"], planets[str(i+1)]["y"], centre)
                pygame.draw.line(screen, (0, 255, 0), start_pos, end_pos)
