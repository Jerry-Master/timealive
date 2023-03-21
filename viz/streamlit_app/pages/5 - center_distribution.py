import streamlit as st
import pandas as pd
import numpy as np
import folium

# Define the coordinates of Catalonia
catalonia_coords = [41.835, 1.757]

# Define a list of 7 random coordinates within Catalonia
coords_list = [[41.5 + np.random.rand()/2, 1.2 + np.random.rand()/2] for i in range(7)]

# Define a list of 7 random sizes for the bubbles
sizes_list = np.random.randint(1, 10, size=7)

# Define a dataframe with the coordinates and sizes
data = pd.DataFrame({
    'lat': [coord[0] for coord in coords_list],
    'lon': [coord[1] for coord in coords_list],
    'size': sizes_list
})

# Create a folium map centered on Catalonia
m = folium.Map(location=catalonia_coords, zoom_start=8)

# Add a circle marker for each coordinate with the corresponding size
for i in range(len(data)):
    folium.CircleMarker(
        location=[data.iloc[i]['lat'], data.iloc[i]['lon']],
        radius=data.iloc[i]['size'] * 5,
        color='blue',
        fill=True,
        fill_color='blue'
    ).add_to(m)

# Display the map in Streamlit
st.markdown('<h1>Map of Catalonia</h1>', unsafe_allow_html=True)
st.markdown(folium.Map(location=catalonia_coords, zoom_start=8)._repr_html_(), unsafe_allow_html=True)

