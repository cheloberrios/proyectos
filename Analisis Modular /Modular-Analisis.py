import streamlit as st
import pandas as pd
import nltk
from plotly import graph_objects as go
import matplotlib.pyplot as plt
import plotly.figure_factory as ff
import numpy as np




modular  = pd.read_csv("Modular3.csv", sep=";")

st.header('Analisis de modular')


modular.drop(columns=["Record ID - Contact"], inplace=True)
modular["Edad (HH:mm:ss)"].notnull().sum()
modular["Edad2"].notnull().sum()
modular["Edad2"].notnull().sum()
modular["Modular"].notnull().sum()

interesados = modular["Correo"].notnull().sum()

precio = modular["Precio modular"].notnull().sum()

evaluacion = modular["¿Qué aspectos te gustaron? Modular"].notnull().sum()

PRECIO = modular["Precio modular"]


edad = modular["Edad2"]


modular

# Add histogram data
x1 = np.random.randn(200) - 2
x2 = np.random.randn(200)
x3 = np.random.randn(200) + 2

# Group data together
hist_data = [x1, x2, x3]

group_labels = ['Group 1', 'Group 2', 'Group 3']

# Create distplot with custom bin_size
fig = ff.create_distplot(
        hist_data, group_labels, bin_size=[.1, .25, .5])

# Plot!
st.plotly_chart(fig, use_container_width=True)


#fig = go.Figure(go.Funnel(
 #   y = ["Interesados", "Interesados con precio", "Interesados con evaluación"],
 #   x = [interesados, precio, evaluacion],
 #   textposition = "inside",
 #   textinfo = "value+percent initial",
  #  opacity = 0.75, marker = {"color": ["blue", "royalblue", "deepskyblue", "silver"],
 #   "line": {"width": [0], "color": ["wheat", "wheat", "blue", "wheat", "wheat"]}},
 #   connector = {"line": {"color": "royalblue", "dash": "dot", "width": 1}})
 #   )

#st.pyplot(p.fig)
