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
line_number_start: 5
line_highlights: 9-31,36
---
def preload():
    global world_map
    world_map = load_image('mercator.jpeg')

def draw_ufo(shape, x, y):
    no_stroke()                  # Turn off outlines
    if shape == 'fireball':
        fill(252, 186, 3)        # Fireball colour
        ellipse(x, y, 15, 10)    # Wide oval
    elif shape == 'circle':
        fill(32, 201, 49)        # Circle colour
        ellipse(x, y, 8, 8)      # Small circle
    elif shape == 'triangle':
        fill(241, 245, 32)       # Triangle colour
        triangle(x - 8, y - 15, x, y, x + 8, y - 15)  # Triangle marker
    elif shape == 'light':
        fill(247, 247, 245)      # Light colour
        ellipse(x, y, 15, 15)    # Large circle
    elif shape == 'disk':
        fill(189, 189, 172)      # Disk colour
        ellipse(x, y, 20, 10)    # Flat oval
    elif shape == 'cylinder' or shape == 'cigar':
        fill(73, 99, 230)        # Cylinder colour
        rect(x, y, 20, 10)       # Rectangle marker
    else:
        fill(255, 0, 0)          # Default colour
        ellipse(x, y, 10, 10)    # Default marker

def draw_data():
    for sighting in ufo_sightings:
        coords = get_xy_coords(float(sighting['longitude']), float(sighting['latitude']))
        draw_ufo(sighting['shape'], coords['x'], coords['y'])  # Draw the matching shape

def setup():
    size(991, 768)
    image(world_map, 0, 0, width, height)
    load_data('ufo-sightings.csv')
    draw_data()

run()

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
