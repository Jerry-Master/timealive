import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Data
data1 = {
    'Mes': [1, 2, 3, 4 , 5, 6, 7 , 8 , 9 , 10 , 11, 12],
    'BASELINE_LONGITUDINALITAT': [0, 0.441734766, 0.441734766,  0, 0, 0, 0, 0, 0, 0, 0, 0],
    'MODEL_LONGITUDINALITAT': [1.0, 1.0, 1.0,  1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0, 1.0]
}

# Create a DataFrame
df1 = pd.DataFrame(data1)

# Create the figure and axes for line plot
fig1, ax1 = plt.subplots()

# Plot the data for line plot
ax1.plot(data1['Mes'], data1['BASELINE_LONGITUDINALITAT'], label='Baseline')
ax1.plot(data1['Mes'], data1['MODEL_LONGITUDINALITAT'], label='Model')

# Customize the line plot
ax1.set_xlabel('Month')
ax1.set_ylabel('Continuity')
ax1.set_title('Evaluation of Continuity')
ax1.legend()
st.pyplot(fig1)

data2 = {
    'Mes': [1, 2, 3, 4 , 5, 6, 7 , 8 , 9 , 10 , 11, 12],
    'BASELINE_TEMPS_ESPERA': [2.1840, 1.9352701, 1.9352701, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'MODEL_TEMPS_ESPERA': [0.3585, 0.0, 0.0, 0, 0, 0, 0, 0, 0 ,0 ,0 ,0]
}

# Create a DataFrame
df2 = pd.DataFrame(data2)

# Create the figure and axes for line plot
fig1, ax1 = plt.subplots()

# Plot the data for line plot
ax1.plot(data2['Mes'], data2['BASELINE_TEMPS_ESPERA'], label='Baseline')
ax1.plot(data2['Mes'], data2['MODEL_TEMPS_ESPERA'], label='Model')

# Customize the line plot
ax1.set_xlabel('Month')
ax1.set_ylabel('Waiting Time')
ax1.set_title('Evaluation of Waiting Time')
ax1.legend()
st.pyplot(fig1)
