import folium

# Dictionary with city names as keys and their coordinates as values
cities = {
    'New York': [40.7128, -74.0060],
    'Los Angeles': [34.0522, -118.2437],
    'Chicago': [41.8781, -87.6298]
}

# Create the map
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)  # USA coordinates

# Add markers to the map using the dictionary
for city, coord in cities.items():
    folium.Marker(location=coord, popup=city).add_to(m)

m.save('map_dictionary.html')
