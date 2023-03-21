import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz')
@st.cache_data
def load_data(nrows):
	'''plain old function that downloads some data, puts it in a Pandas dataframe, and converts the date column from text to datetime'''
	data = pd.read_csv(DATA_URL, nrows=nrows) #llegeix les dades
	lowercase = lambda x: str(x).lower() #defineix la funció per pasar dades a minuscules
	data.rename(lowercase, axis='columns', inplace=True) #fa un renaming de les dades a minuscules
	data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN]) #transforma les dades a fechas (datetime)
	return data

# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text("Done! (using st.cache_data)")

#looking at raw data
#st.subheader('Raw data')
#st.write(data) #rendered as an interactive table

#usar un boton para alternar datos
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

#draw a histogram
st.subheader('Number of pickups by hour')
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
st.bar_chart(hist_values)

#plot data on a map
#st.subheader('Map of all pickups')
#st.map(data)
#filter data with a slider
hour_to_filter = st.slider('hour', 0, 23, 17)  # min: 0h, max: 23h, default: 17h
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]
st.subheader(f'Map of all pickups at {hour_to_filter}:00')
st.map(filtered_data)

