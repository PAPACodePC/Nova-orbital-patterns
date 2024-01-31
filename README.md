# NOVA-ORBITAL-PATTERNS 

## Project Guide
This project, taken on with my daughter, has been a delightful journey through various iterations, each bringing its own set of improvements and excitement.

The repository serves as a foundational guide to enhance the existing application by adding features like color strobes, rainbow strobes, sequential rainbow coloration by line, buttons, sliders, and improved modularity for easier variable configuration and user interface navigation.

## Step 1: Clone the Repository
- Clone the repository from [plusk-dev/orbital-patterns on GitHub](https://github.com/plusk-dev/orbital-patterns).
- Install the required dependencies: Review the "requirements.txt" file and run `pip install pygame==2.5.2`.

## Step 2: Run the Original Application
- Ensure all dependencies are correctly installed.
- Review the original `ReadMe.md` for any additional notes.
- Run the `Original_main.py` file to understand the current state of the project.

**Original Orbital Patterns Features:**
- Click to spawn planets.
- Press "S" to capture a screenshot, which saves in the script directory.
- Press "Q" to exit.
- Press "A" to display axes and a line joining the origin to your cursor.

![Original Orbital Patterns](https://images-ext-2.discordapp.net/external/reeKlQI6RiU9At2H5C-73ryCnpLqL4ru7shOThJFGdw/https/repository-images.githubusercontent.com/445509211/95c2a5b3-2bb4-4aad-8acf-1209bf9700ec)

## Step 3: Overview of the Current Script
The Python script is a basic orbit visualizer created with Pygame, simulating and visualizing the motion of celestial bodies. Key features include:

1. **Pygame Initialization**: Setting up a full-screen display and defining screen dimensions and center point.

2. **Global Variables and Functions**: Includes a dictionary for planets, a function to convert coordinates, and the `render` function for screen updates.

3. **Orbit Calculation and Rendering**: Updates planet positions based on angular velocity, draws planets and their orbits, and shows relative positions over time with connecting lines.

4. **Interactive Elements**: Allows toggling axes display, saving screenshots, and adding new planets with mouse clicks.

5. **Main Loop**: Continuously handles events and updates the display while maintaining frame rate.

### Possible Enhancements:
- **User Interface**: More interactive elements for planet management and simulation control.
- **Physics Accuracy**: Improved orbital mechanics, including elliptical orbits and gravitational interactions.
- **Performance Optimization**: Necessary for handling numerous planets.
- **Visual Improvements**: Diverse colors, sizes, and additional celestial objects for a richer visual experience.

## Step 4: Show Appreciation
Before diving into enhancements, it's crucial to acknowledge and appreciate the work of the original developers. Most foundational work has been done, and it's respectful to give credit where it's due.

**Special Thanks to:**
- [plusk-dev on GitHub](https://github.com/plusk-dev)
- [kirbyyourmom on GitHub](https://github.com/kirbyyourmom)

---
