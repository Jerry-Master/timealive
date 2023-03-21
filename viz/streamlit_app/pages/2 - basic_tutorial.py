"""
# My first app
Here's our first attempt at using data to create a table:
"""

import streamlit as st
import numpy as np
import pandas as pd
"""
import pickle
import time
from matplotlib import pyplot as plt
from  matplotlib.ticker import FuncFormatter
import seaborn as sns
import os
"""


st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# st.dataframe() and st.table() son altres funcions que serveixen per mostrar dades. 
# st.table() es per taules estatiques mentre que write es per dataframes dinamics. 
# "Styler" object to change format with Pandas. 

dataframe = pd.DataFrame(
    np.random.randn(10, 20),
    columns=('col %d' % i for i in range(20)))
st.dataframe(dataframe.style.highlight_max(axis=0)) #highlight some elements in the interactive table.

# Draw a line chart

st.write("We will print a line chart")
chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# Plot a map

st.write("We will print a line chart")
map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [41.38, 2.15],
    columns=['lat', 'lon'])
st.map(map_data) #printa un mapa de San Francisco con puntos distribuidos de manera random centrados en cierto valor de long/lat 

#Widgets
#add in widgets like st.slider(), st.button() or st.selectbox()

x = st.slider('x')  # 👈 this is a widget
st.write(x, 'al cuadrado es = ', x * x)

#les widgets poden ser accessibles per key, es a dir , si escollim string especifica com una key unica per una widget : 

st.text_input("Your name", key="name") #pregunta por tu nombre y escribe ese mismo valor (key)
# You can access the value at any point with:
st.session_state.name

#use checkboxes to show/hide data

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data

#select box

df = pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
    })

option = st.selectbox(
    'Which number do you like best?',
     df['first column'])

'You selected: ', option

#Layout 
#usem st.sidebar.slider and st.sidebar.selectbox instead of st.slider and st.selectbox si volem afegirles a una barra lateral en canvi de original. 

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

#other options to control layout of the app 
# st.columns per situar widgets side-by-side
# st.expanders et permet conservar espai amagant el contingut gran. 

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")

#show progress
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'


#Themes 

#caching
@st.cache_data
def long_running_function(param1, param2):
    return None

#st.cache_resource es una alternativa a cache_data que va millor alhora de fer cache de global resources com ara ML models o connexions de bases de dades. 
#es a dir, objectes no-serializatbles que no volem carregar multiples vegades. 
