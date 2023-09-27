import googlemaps
from time import sleep

gmaps = googlemaps.Client(key='')

# Manhattan, canal street soho off the Q
location = (40.75, -74)
# Radius in meters
radius = 5000

# Initialize variables
page_token = None
filtered_places = []

while len(filtered_places) < 20:
    # Make a request to the Places API
    places_result = gmaps.places_nearby(
        location=location,
        radius=radius,
        type='restaurant',
        page_token=page_token,
    )

    # Add a delay of a few seconds before making the next request
    sleep(4)

    # Iterate through the results and filter places with ratings higher than 4.9
    for place in places_result.get('results', []):
        print(place.get('rating'))
        if place.get('rating') >= 4.7:
            filtered_places.append(place)

    # Check if there are more pages of results
    page_token = places_result.get('next_page_token')
    if not page_token:
        break

# Print the filtered places
for place in filtered_places:
    print(f"Name: {place['name']}, Rating: {place.get('rating', 'N/A')}")
