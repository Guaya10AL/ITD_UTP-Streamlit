import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn import datasets

# Title of the app
st.title("Avance Trabajo 3")

# Header
st.header("Esta es una aplicación de Streamlit con Machine Learning")

# Leer el dataset
df = pd.read_csv("dataset.csv", encoding="latin-1",sep=";")

# Mostrar los datos en una tabla
st.subheader("Datos del conjunto de datos")
st.dataframe(df)

# Mostrar gráfico de dispersión
st.subheader("Gráfico de dispersión")
x_column = st.selectbox("Seleccionar columna para el eje x", df.columns)
y_column = st.selectbox("Seleccionar columna para el eje y", df.columns)
plt.figure(figsize=(8, 6))
plt.scatter(df[x_column], df[y_column])
plt.xlabel(x_column)
plt.ylabel(y_column)
st.pyplot(plt)

# Mostrar histograma
st.subheader("Histograma")
column = st.selectbox("Seleccionar columna para el histograma", df.columns)
plt.figure(figsize=(8, 6))
sns.histplot(df[column], kde=True)
plt.xlabel(column)
plt.ylabel("Frecuencia")
st.pyplot(plt)

# Mostrar gráfico de barras
st.subheader("Gráfico de barras")
column = st.selectbox("Seleccionar columna para el gráfico de barras", df.columns)
counts = df[column].value_counts()
plt.figure(figsize=(8, 6))
sns.barplot(x=counts.index, y=counts.values)
plt.xlabel(column)
plt.ylabel("Frecuencia")
plt.xticks(rotation=45)
st.pyplot(plt)}
