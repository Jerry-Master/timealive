import streamlit as st
import pandas as pd
import numpy as np
import os


st.title('Visits_dataset')

DATE_COLUMN = 'date/time'
STREAMLIT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(STREAMLIT_DIR, 'data', 'visites_coord.csv')

def load_data(nrows):
	'''plain old function that downloads some data, puts it in a Pandas dataframe, and converts the date column from text to datetime'''
	data = pd.read_csv(DATA_PATH, nrows=nrows, encoding='latin') #llegeix les dades
	#lowercase = lambda x: str(x).lower() #defineix la funció per pasar dades a minuscules
	#data.rename(lowercase, axis='columns', inplace=True) #fa un renaming de les dades a minuscules
	#data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN]) #transforma les dades a fechas (datetime)
	return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

st.write(type(data["Hora"]))

#looking at raw data
#st.subheader('Raw data')
#st.write(data) #rendered as an interactive table

#usar un boton para alternar datos
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#draw a histogram
st.subheader('Number of visits by hour')
hist_values = np.histogram(
    int(data["Hora"][:2]), bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

#plot data on a map
#st.subheader('Map of all pickups')
#st.map(data)
#filter data with a slider
hour_to_filter = st.slider('hour', 0, 23, 12)  # min: 0h, max: 23h, default: 17h
filtered_data = data[int(data["Hora"][:2]) == hour_to_filter]
st.subheader(f'Map of all visits at {hour_to_filter}:00')
st.map(filtered_data)

