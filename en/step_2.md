<h2 class="c-project-heading--task">Import p5 and the coordinate helper</h2>

--- task ---
Import p5 and the function that converts latitude/longitude into x/y coordinates.
--- /task ---

The `xy.py` file contains a function called `get_xy_coords()` that converts latitude and longitude into pixel coordinates on the map.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 2-3
---

#!/bin/python3
from p5 import *
from xy import get_xy_coords

--- /code ---
</div>

--- task ---
**Test:** Run your code.  
It should run without errors (it will not draw anything yet).
--- /task ---

<div class="c-project-callout c-project-callout--debug">

### Debugging

- If you see `No module named 'xy'`, check that `xy.py` is in the project folder

</div>
