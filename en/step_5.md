<h2 class="c-project-heading--task">Load UFO data from the CSV file</h2>

--- task ---
Read the UFO sightings CSV and store each row.
--- /task ---

You will store sightings in a list so you can draw them later.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 9-24,29-30
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

def setup():
    size(991, 768)               # Set the size of the drawing window
    image(world_map, 0, 0, width, height)  # Draw the map to fill the window

    load_data('ufo-sightings.csv')  # Load the UFO sighting data
    print(ufo_sightings[0])         # Print the first sighting to check it loaded

run()                            # Start the p5 sketch

--- /code ---
</div>


--- task ---
**Test:** Run your code.  

--- /task ---

--- task ---

Click on the `Text Output` tab above the map. You should see the data for one sighting printed in the output.

--- /task ---

<div class="c-project-output">
<pre><img
  class="fit-picture"
  src="images/textoutput.png"
  alt=" A dictionary listing for a UFO sighting." />
</pre>
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- If you get `IndexError`, check for blank lines in the CSV, or skip empty lines in your loop

</div>
