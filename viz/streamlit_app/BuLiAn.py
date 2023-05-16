import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Data for line plot
months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
visited_patients = [200, 150, 20, 15, 10, 10, 5, 5, 10, 15, 50, 150]
mean = [250, 200, 30, 30, 30, 20, 20, 20, 10, 10, 100, 200]

# Data for bar plot
visit_types = [
    'ESPONTANIA', 'SEGONA VISITA TABAC', 'PRIMERA VISITA TABAC',
    'AL CENTRE', 'EXT DOMICILI', 'DOMICILIÀRIA', 'ATENCIO DOMICILIARIA',
    'CITA PREVIA', 'TÈCNIQ./PROCEDIMENTS', 'DOMICILI', 'PREALT', 'RECEPTES',
    'RESERV CENTRE', 'TELEFÒNICA', 'NO PRESENCIAL'
]
number_of_visits = [
    98.03921569, 78.43137255, 78.43137255, 84.96732026, 91.50326797,
    91.50326797, 91.50326797, 71.89542484, 58.82352941, 91.50326797,
    19.60784314, 52.2875817, 71.89542484, 6.535947712, 13.07189542
]

# Color labels for the bar plot
color_labels = [
    'red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink',
    'gray', 'olive', 'teal', 'cyan', 'magenta', 'lightblue',
    'lime', 'gold'
]

# Create the figure and axes for line plot
fig1, ax1 = plt.subplots()

# Plot the data for line plot
ax1.plot(months, visited_patients, label='Visited Patients')
ax1.plot(months, mean, label='Mean')

# Customize the line plot
ax1.set_xlabel('Month')
ax1.set_ylabel('Visited Patients')
ax1.set_title('Visited Patients per Month')
ax1.legend()

# Sort the visit types and number of visits in descending order
sorted_indices = np.argsort(number_of_visits)[::-1]
sorted_visit_types = [visit_types[i] for i in sorted_indices]
sorted_number_of_visits = [number_of_visits[i] for i in sorted_indices]
sorted_color_labels = [color_labels[i] for i in sorted_indices]


# Create the figure and axes for bar plot
fig2, ax2 = plt.subplots()

# Plot the data for bar plot
ax2.bar(sorted_visit_types, sorted_number_of_visits)

# Customize the bar plot
ax2.set_xlabel('Type of Visits')
ax2.set_ylabel('Number of Visits')
ax2.set_title('Number of Visits by Visit Type')
ax2.set_xticklabels(sorted_visit_types, rotation=90)

# Create the figure and axes for bar plot
fig3, ax3 = plt.subplots()

# Plot the data for bar plot with color labels
bars = ax3.bar(sorted_visit_types, sorted_number_of_visits, color=sorted_color_labels)

# Customize the bar plot
ax3.set_xlabel('Type of Visits')
ax3.set_ylabel('Number of Visits')
ax3.set_title('Number of Visits per Type')
ax3.set_xticklabels(sorted_visit_types, rotation=90)

# Add color labels to the legend
legend_labels = [f'{visit_type}: {number_of_visits:.2f}%' for visit_type, number_of_visits in zip(sorted_visit_types, sorted_number_of_visits)]
ax3.legend(bars, legend_labels)

import streamlit as st
import matplotlib.pyplot as plt

# Data
data = {
    'ESPONTANIA': 98.03921569,
    'DOMICILI': 91.50326797,
    'EXT DOMICILI': 91.50326797,
    'DOMICILIÀRIA': 91.50326797,
    'ATENCIO DOMICILIARIA': 91.50326797,
    'AL CENTRE': 84.96732026,
    'SEGONA VISITA TABAC': 78.43137255,
    'PRIMERA VISITA TABAC': 78.43137255,
    'CITA PREVIA': 71.89542484,
    'RESERV CENTRE': 71.89542484,
    'TÈCNIQ./PROCEDIMENTS': 58.82352941,
    'RECEPTES': 52.2875817,
    'PREALT': 19.60784314,
    'NO PRESENCIAL': 13.07189542,
    'TELEFÒNICA': 6.535947712
}

# Convert the dictionary to two separate lists
labels = list(data.keys())
values = list(data.values())

# Create a pie chart
fig4, ax4 = plt.subplots()
ax4.pie(values, labels=labels, autopct='%1.1f%%', startangle=90)
ax4.set_aspect('equal')  # Equal aspect ratio ensures that pie is drawn as a circle
ax4.set_title('Type of Visits')

# Display the plots using Streamlit
st.pyplot(fig1)
st.pyplot(fig2)
st.pyplot(fig3)
st.pyplot(fig4)



