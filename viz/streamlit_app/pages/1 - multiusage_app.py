import streamlit as st
import pandas as pd
import numpy as np
import folium

# Data
data = [
    {"Codi EAP": 151, "Nombre del CAP": "EAP CORNELLÀ DE LLOBREGAT 1 MARTÍ JULIÀ", "SAP nom": "Baix Llobregat Centre", "Codi SAP": 13, "latitude": 41.3535, "longitude": 2.06662},
    {"Codi EAP": 153, "Nombre del CAP": "EAP CORNELLÀ DE LLOBREGAT 3 GAVARRA", "SAP nom": "Baix Llobregat Centre", "Codi SAP": 13, "latitude": 41.35561, "longitude": 2.07043},
    {"Codi EAP": 161, "Nombre del CAP": "EAP HOSPITALET DE LLOBREGAT 10 CAN SERRA", "SAP nom": "Delta litoral", "Codi SAP": 57, "latitude": 41.3661, "longitude": 2.09997},
    {"Codi EAP": 170, "Nombre del CAP": "EAP PENEDÈS RURAL", "SAP nom": "Alt Penedès Garraf", "Codi SAP": 17, "latitude": 41.3444241, "longitude": 1.6995284},
    {"Codi EAP": 172, "Nombre del CAP": "EAP EL PRAT DE LLOBREGAT 2 SANT COSME I", "SAP nom": "Delta litoral", "Codi SAP": 57, "latitude": 41.3160855, "longitude": 2.0867355},
    {"Codi EAP": 173, "Nombre del CAP": "EAP EL PRAT LLOBREGAT 3 PUJOL I CAPÇADA", "SAP nom": "Delta litoral", "Codi SAP": 57, "latitude": 41.32784, "longitude": 2.09472},
    {"Codi EAP": 176, "Nombre del CAP": "EAP SANT BOI DE LLOBREGAT 3 CAMPS BLANCS", "SAP nom": "Baix Llobregat Centre", "Codi SAP": 13, "latitude": 41.3376973, "longitude": 2.0295362},
    {"Codi EAP": 177, "Nombre del CAP": "EAP SANT JOAN DESPÍ 2 LES PLANES", "SAP nom": "Baix Llobregat Centre", "Codi SAP": 13, "latitude": 41.3671859, "longitude": 2.0730109},
    {"Codi EAP": 183, "Nombre del CAP": "EAP VILADECANS 2", "SAP nom": "Delta litoral", "Codi SAP": 57, "latitude": 41.3163083, "longitude": 2.0156034},
    {"Codi EAP": 193, "Nombre del CAP": "EAP HOSPITALET LLOBREGAT 9 PUBILLA CASES", "SAP nom": "Delta litoral", "Codi SAP": 57, "latitude": 41.3734592, "longitude": 2.1063928},
    {"Codi EAP": 197, "Nombre del CAP": "EAP SANT BOI DE LLOBREGAT 1 MONTCLAR", "SAP nom": "Baix Llobregat Centre", "Codi SAP": 13, "latitude": 41.3446122, "longitude": 2.0381487},
    {"Codi EAP": 200, "Nombre del CAP": "EAP SANT FELIU DE LLOBREGAT 2 RAMBLA", "SAP nom": "Baix Llobregat Centre", "Codi SAP": 13, "latitude": 41.3831529, "longitude": 2.0504115},
    {"Codi EAP": 206, "Nombre del CAP": "EAP VILANOVA I LA GELTRÚ 2", "SAP nom": "Alt Penedès Garraf", "Codi SAP": 17, "latitude": 41.2241992, "longitude": 1.7256327},
    {"Codi EAP": 4546, "Nombre del CAP": "EAP ABRERA", "SAP nom": "Baix Llobregat Nord", "Codi SAP": 16, "latitude": 41.5204464, "longitude": 1.9024126},
    {"Codi EAP": 4819, "Nombre del CAP": "EAP MARTORELL RURAL", "SAP nom": "Baix Llobregat Nord", "Codi SAP": 16, "latitude": 41.47402, "longitude": 1.93062},
    {"Codi EAP": 5239, "Nombre del CAP": "EAP BEGUES. POU TORRE", "SAP nom": "Delta litoral", "Codi SAP": 57, "latitude": 41.3328119, "longitude": 1.925468},
    {"Codi EAP": 7961, "Nombre del CAP": "EAP VILAFRANCA DEL PENEDÈS 1", "SAP nom": "Alt Penedès Garraf", "Codi SAP": 17, "latitude": 41.3530923, "longitude": 1.7068573},
    {"Codi EAP": 8117, "Nombre del CAP": "EAP RIBES-OLIVELLA", "SAP nom": "Alt Penedès Garraf", "Codi SAP": 17, "latitude": 41.2292796, "longitude": 1.7459127}
]

st.map(data)

# Add tooltips to display information on hover
for entry in data:
    name = entry['Nombre del CAP']
    lat = entry['latitude']
    lon = entry['longitude']
    tooltip = f"Nombre del CAP: {name}"
    st.write(f"* Latitude: {lat}, Longitude: {lon}", unsafe_allow_html=True, key=tooltip)


# Data
data1 = {
    'Mes': [1, 2, 3],
    'BASELINE_LONGITUDINALITAT': [0, 0.441734766, 0.441734766],
    'MODEL_LONGITUDINALITAT': [1.0, 1.0, 1.0]
}

# Create a DataFrame
df1 = pd.DataFrame(data1)

data2 = {
    'Mes': [1, 2, 3],
    'BASELINE_TEMPS_ESPERA': [2.1840, 1.9352701, 1.9352701],
    'MODEL_TEMPS_ESPERA': [0.3585, 0.0, 0.0]
}

# Create a DataFrame
df2 = pd.DataFrame(data2)

# Set the 'Mes' column as the index
df1.set_index('Mes', inplace=True)
df2.set_index('Mes', inplace=True)


# Create two columns for the line charts
col1, col2 = st.beta_columns(2)

# Create the chart
st.line_chart(df1)
st.line_chart(df2)
