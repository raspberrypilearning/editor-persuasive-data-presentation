<h2 class="c-project-heading--task">Load and display the map</h2>

--- task ---
Load the map image and display it in a p5 window.
--- /task ---

Use `preload()` to load the image before your sketch starts, then show it in `setup()`.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 5-18
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

run()

--- /code ---
</div>

--- task ---
**Test:** Run your code.  
You should see the world map.
--- /task ---

<div class="c-project-output">
<pre>A world map image fills the window.</pre>
</div>
