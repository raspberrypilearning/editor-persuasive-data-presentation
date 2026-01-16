<!-- step_8.md -->
<h2 class="c-project-heading--task">Make markers clickable</h2>

--- task ---
Print a message when the user clicks on a UFO marker.
--- /task ---

You will:
- Draw different coloured markers for different UFO shapes
- Detect the colour of the pixel under the mouse pointer
- Print a message based on the colour that was clicked

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 7, 10, 13, 16, 19, 22, 25,54-71, 76-83
---
from p5 import *                 # Import p5 so we can draw graphics
from xy import get_xy_coords     # Import helper to convert latitude/longitude to x/y

def draw_ufo(shape, x, y):      # Draw the UFO on the map    
    no_stroke()     
    if shape == 'fireball':
        fill(fireball)          # Use the colour variable below
        ellipse(x, y, 15, 10)
    elif shape == 'circle':
        fill(circle)          # Use the colour variable below
        ellipse(x, y, 8, 8)
    elif shape == 'triangle':
        fill(tri)          # Use the colour variable below
        triangle(x-8, y-15, x, y, x+8, y-15)
    elif shape == 'light':
        fill(light)          # Use the colour variable below
        ellipse(x, y, 15, 15)
    elif shape == 'disk':
        fill(disk)          # Use the colour variable below
        ellipse(x, y, 20, 10)
    elif shape == 'cylinder' or shape == 'cigar':
        fill(cylinder)          # Use the colour variable below
        rect(x, y, 20, 10)
    else:
        fill(misc)          # Use the colour variable below
        ellipse(x, y, 10, 10)

def preload():
    global map                   # Make the map image available to the whole program
    map = load_image('mercator.jpeg')  # Load the map image before drawing starts

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

def draw_data():
    for sighting in ufo_sightings:  # Draw one marker for each sighting
        coords = get_xy_coords(float(sighting['longitude']), float(sighting['latitude']))  # Convert lat/long to x/y
        draw_ufo(sighting['shape'], coords['x'], coords['y'])  # Draw the correct marker for the shape

def mouse_pressed():        # Display a message depending on what shape the user has pressed
    pixel_colour = Color(get(mouse_x, mouse_y)).hex  # Get the colour where the user clicked
    if pixel_colour == fireball.hex:
        print('A fireball UFO was spotted here!')
    elif pixel_colour == circle.hex:
        print('A circle shaped UFO was spotted here!')
    elif pixel_colour == tri.hex:
        print('A triangle shaped UFO was spotted here!')
    elif pixel_colour == light.hex:
        print('A UFO made of light was spotted here!')
    elif pixel_colour == disk.hex:
        print('A disk shaped UFO was spotted here!')
    elif pixel_colour == misc.hex:
        print('A random shaped UFO was spotted here!')
    elif pixel_colour == cylinder.hex:
        print('A cylinder shaped UFO was spotted here!')
    else:
        print('There were no UFO sightings in this area!')

def setup():
    global fireball, circle, tri, light, disk, misc, cylinder  # Store colours so clicks can be checked later
    
    fireball = Color(252, 186, 3)   # Colour for fireball sightings
    circle = Color(32, 201, 49)     # Colour for circle sightings
    tri = Color(241, 245, 32)       # Colour for triangle sightings
    light = Color(247, 247, 245)    # Colour for light sightings
    disk = Color(189, 189, 172)     # Colour for disk sightings
    misc = Color(255, 0, 0)         # Default colour for other shapes
    cylinder = Color(73, 99, 230)   # Colour for cylinder/cigar sightings
    
    size(991, 768)               # Set the size of the drawing window
    load_data('ufo-sightings.csv')  # Load the UFO sighting data
    image(map, 0, 0, width, height)  # Draw the map to fill the window
    draw_data()                  # Plot the UFO sightings

run()                            # Start the p5 sketch

--- /code ---
</div>


--- task ---
**Test:** Run your code, then click on different markers.  
You should see different messages in the output depending on what you clicked.
--- /task ---

<div class="c-project-output">
<pre><img
  class="fit-picture"
  src="images/mapclick.gif"
  alt=" A world map with many small multicoloured dots appearing on the map in different shapes. The user clicks a dot and gets shown wirtten text." />
</pre>
</div>


<div class="c-project-callout c-project-callout--debug">

### Debugging

- If clicking always prints “There were no UFO sightings in this area!”, check that the map image is drawn **before** `draw_data()`
- If you see an error about `color` or `null`, make sure the sketch is running and the window has loaded before clicking
- If every click says “no sightings”, check the markers are drawn after the map image
- If colours never match, check you are using the same `Color(...)` objects for drawing and comparison

</div>



