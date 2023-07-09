##########################################################
#######[1] PAQUETE
##########################################################
import streamlit as st
from PIL import Image
#@st.cache 
##########################################################
#######[2]FILTROS PRINCIPALES
##########################################################

image = Image.open('Minedu.png')
st.image(image, caption='',use_column_width=True)

st.title("Test de Minedu 2020 :sunglasses:")

