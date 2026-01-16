<h2 class="c-project-heading--task">Draw different markers for different UFO shapes</h2>

--- task ---
Draw a different marker depending on the reported UFO shape.
--- /task ---

The dataset includes a `shape` field. You can use it to draw different symbols and colours.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 23-47,55
---
#!/bin/python3
from p5 import *                 # Import p5 so we can draw graphics
from xy import get_xy_coords     # Import helper to convert latitude/longitude to x/y

def preload():
    global world_map             # Make the map image available to the whole program
    world_map = load_image('mercator.jpeg')  # Load the map image before drawing starts

def load_data(file_name):
    global ufo_sightings         # Store all sightings so other functions can use them
    ufo_sightings = []           # Start with an empty list
    with open(file_name) as f:   # Open the CSV file
        for line in f:           # Read the file one line at a time
            info = line.strip().split(',')  # Split the line into columns
            ufo_sightings.append({          # Store one sighting as a dictionary
                'date': info[0],
                'time': info[1],
                'state': info[2],
                'country': info[3],
                'shape': info[4],
                'duration': info[5],
                'latitude': info[6],
                'longitude': info[7]
            })

def draw_ufo(shape, x, y):
    no_stroke()                  # Turn off outlines so the shapes are clearer
    if shape == 'fireball':
        fill(252, 186, 3)        # Set the colour for fireball sightings
        ellipse(x, y, 15, 10)    # Draw a wider oval
    elif shape == 'circle':
        fill(32, 201, 49)        # Set the colour for circle sightings
        ellipse(x, y, 8, 8)      # Draw a small circle
    elif shape == 'triangle':
        fill(241, 245, 32)       # Set the colour for triangle sightings
        triangle(x - 8, y - 15, x, y, x + 8, y - 15)  # Draw a triangle marker
    elif shape == 'light':
        fill(247, 247, 245)      # Set the colour for light sightings
        ellipse(x, y, 15, 15)    # Draw a larger circle
    elif shape == 'disk':
        fill(189, 189, 172)      # Set the colour for disk sightings
        ellipse(x, y, 20, 10)    # Draw a flat oval
    elif shape == 'cylinder' or shape == 'cigar':
        fill(73, 99, 230)        # Set the colour for cylinder/cigar sightings
        rect(x, y, 20, 10)       # Draw a rectangle marker
    else:
        fill(255, 0, 0)          # Use a default colour for other shapes
        ellipse(x, y, 10, 10)    # Draw a default marker

def draw_data():
    for sighting in ufo_sightings:  # Draw one marker for each sighting
        coords = get_xy_coords(float(sighting['longitude']), float(sighting['latitude']))  # Convert lat/long to x/y
        draw_ufo(sighting['shape'], coords['x'], coords['y'])  # Draw the correct marker for the shape

def setup():
    size(991, 768)               # Set the size of the drawing window
    image(world_map, 0, 0, width, height)  # Draw the map to fill the window

    load_data('ufo-sightings.csv')  # Load the UFO sighting data
    draw_data()                     # Plot the sightings using different markers

run()                            # Start the p5 sketch

--- /code ---
</div>


--- task ---
**Test:** Run your code.  
Markers should now vary by colour and shape.
--- /task ---

<div class="c-project-output">
<pre><img
  class="fit-picture"
  src="images/colour-dots.png"
  alt=" A world map with many small multicoloured dots appearing on the map in different shapes." />
</pre>
</div>