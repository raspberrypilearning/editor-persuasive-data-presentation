<h2 class="c-project-heading--task">Import p5 and the coordinate helper</h2>

--- task ---
Import p5 and the function that converts latitude and longitude into x/y screen coordinates.
--- /task ---

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
from p5 import *                 # Import p5 so we can draw shapes and images
from xy import get_xy_coords     # Import a helper function to convert lat/long to x/y

--- /code ---
</div>

--- task ---
**Test:** Click **Run**.

The program should run without errors, but nothing will appear yet because no drawing code has been added.
--- /task ---
