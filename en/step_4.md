<!-- step_4.md -->
<h2 class="c-project-heading--task">Test coordinate conversion with one marker</h2>

--- task ---
Convert one latitude/longitude pair into x/y coordinates and draw a marker.
--- /task ---

Before reading the dataset, test the conversion with a single known location.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 12-18
---

#!/bin/python3
from p5 import *
from xy import get_xy_coords

def preload():
    global world_map
    world_map = load_image('mercator.jpeg')

def setup():
    size(991, 768)
    image(world_map, 0, 0, width, height)

    coords = get_xy_coords(-0.1276, 51.5072)  # longitude, latitude (London)
    fill(255, 0, 0)
    no_stroke()
    ellipse(coords['x'], coords['y'], 8, 8)

run()

--- /code ---
</div>

--- task ---
**Test:** Run your code.  
A red dot should appear around the UK.
--- /task ---

<div class="c-project-output">
<pre><img
  class="fit-picture"
  src="images/ukdot.png"
  alt=" A red dot appears over the UK" />
</pre>
</div>

<div class="c-project-callout c-project-callout--tip">

### Tip

If the dot appears in the wrong place, check you are passing:
- longitude first
- latitude second

</div>
