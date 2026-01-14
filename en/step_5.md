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
line_highlights: 9-30,35
---

#!/bin/python3
from p5 import *
from xy import get_xy_coords

def preload():
    global world_map
    world_map = load_image('mercator.jpeg')

def load_data(file_name):
    global ufo_sightings
    ufo_sightings = []

    with open(file_name) as f:
        for line in f:
            info = line.strip().split(',')
            ufo_sightings.append({
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
    size(991, 768)
    image(world_map, 0, 0, width, height)

    load_data('ufo-sightings.csv')
    print(ufo_sightings[0])

run()

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
