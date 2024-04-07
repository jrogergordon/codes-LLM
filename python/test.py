import folium

# Coordinates (latitude and longitude)
locations = [[40.7128, -74.0060, 'New York'], 
             [34.0522, -118.2437, 'Los Angeles'], 
             [41.8781, -87.6298, 'Chicago']]

# Create the map
m = folium.Map(location=[39.8283, -98.5795], zoom_start=4)

# Add markers with custom icons and popups
for loc in locations:
    folium.Marker(
        location=[loc[0], loc[1]],
        popup=f'<strong>{loc[2]}</strong>',
        icon=folium.Icon(icon='cloud')
    ).add_to(m)

m.save('map_advanced.html')
