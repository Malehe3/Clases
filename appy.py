import streamlit as st
from PIL import Image 

st.title("Mi primera chamba!!")

st.header("En este espacio comienzo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo realizar backend y frontend.")
image = Image.open('zy.jpg')

st.image(image, caption='Interfaces multimodales')
