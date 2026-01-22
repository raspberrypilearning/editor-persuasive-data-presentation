def load_data(file_name):
    global ufo_sightings         # Store sightings for other functions
    ufo_sightings = []           # Start with an empty list
    with open(file_name) as f:   # Open the CSV file
        for line in f:           # Read one line at a time
            info = line.strip().split(',')  # Split into columns
            ufo_sightings.append({          # Store one sighting
                'date': info[0],
                'time': info[1],
                'state': info[2],
                'country': info[3],
                'shape': info[4],
                'duration': info[5],
                'latitude': info[6],
                'longitude': info[7]
            })