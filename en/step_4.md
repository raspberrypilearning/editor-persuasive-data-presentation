<h2 class="c-project-heading--task">Load UFO data from the CSV file</h2>

--- task ---
Read the UFO sightings CSV and store each row.
--- /task ---

You will store sightings data from a spreadsheet in a list, so you can use it later. 
Import the `load_data` function from the helper file, then load the data:

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 3,12-13
---
from p5 import *
from xy import get_xy_coords
from load_data import load_data

def preload():
    global world_map
    world_map = load_image('mercator.jpeg')

def setup():
    size(991, 768)
    image(world_map, 0, 0, width, height)
    load_data('ufo-sightings.csv')  # Load the data
    print(ufo_sightings[0])         # Print the first row

run()

--- /code ---
</div>

--- task ---
**Test:** Run your code.
You should see the information in the first line of the spreadsheet `ufo-sightings.csv` written in the Text Output window:

<div class="c-project-output">
<pre><img
  class="fit-picture"
  src="images/textoutput.png"
  alt=" A dictionary listing for a UFO sighting." />
</pre>
</div>

<div class="c-project-callout c-project-callout--debug">

### Debugging

- If you can't see where the output is, click on the `Split view` tab above the map. You should see the data for one sighting printed in the text output.

</div>

--- /task ---

--- task ---

Change the number in `print(ufo_sightings[0])` and run your code again to see different data.

--- /task ---