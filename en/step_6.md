<h2 class="c-project-heading--task">Plot all sightings as simple dots</h2>

--- task ---
Loop through the dataset and draw a dot for each sighting.
--- /task ---

Convert each sighting’s latitude/longitude to x/y coordinates and draw a small marker.

<div class="c-project-code">
--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 21
line_highlights: 25-30,36
---
                'latitude': info[6],
                'longitude': info[7]
            })

def draw_data():
    no_stroke()                  # Turn off outlines so the dots are clearer
    fill(255, 0, 0)              # Set the colour for the markers
    for sighting in ufo_sightings:  # Draw one marker for each sighting
        coords = get_xy_coords(float(sighting['longitude']), float(sighting['latitude']))  # Convert lat/long to x/y
        ellipse(coords['x'], coords['y'], 4, 4)  # Draw a small dot at the location

def setup():
    size(991, 768)               # Set the size of the drawing window
    image(world_map, 0, 0, width, height)  # Draw the map to fill the window
    load_data('ufo-sightings.csv')  # Load the UFO sighting data
    draw_data()                     # Plot the sightings as dots

run()                            # Start the p5 sketch

--- /code ---
</div>


--- task ---
**Test:** Run your code.  
You should see many small red dots on the map.
--- /task ---

<div class="c-project-output">
<pre><img
  class="fit-picture"
  src="images/red-dots.png"
  alt=" A world map with many small red dots appearing on the map." />
</pre>
</div>