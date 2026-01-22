<!-- step_4.md -->
<h2 class="c-project-heading--task">Test coordinate conversion with one marker</h2>

--- task ---
Convert one latitude/longitude pair into x/y coordinates and draw a marker.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 8
line_highlights: 11-14
---
def setup():
    size(991, 768)
    image(world_map, 0, 0, width, height)
    coords = get_xy_coords(-0.1276, 51.5072)  # Convert lon/lat to x/y
    fill(255, 0, 0)             # Red marker colour
    no_stroke()                 # Turn off outlines
    ellipse(coords['x'], coords['y'], 8, 8)  # Draw a test dot

run()

--- /code ---
</div>
--- /task ---

--- task ---
**Test:** Run your code.  
A red dot should appear around the UK.


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

--- /task ---

--- task ---

Go to [google maps](https://www.google.com/maps){:target="_blank"} and find more coordinates to try in your code!

<div class="c-project-callout c-project-callout--tip">

### Tip

- Change the numbers in `coords = get_xy_coords(-0.1276, 51.5072)` to move the marker.

</div>

--- /task ---