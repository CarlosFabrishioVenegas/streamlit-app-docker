import streamlit as st
from transformers import pipeline
from utils import generate_image, classify_image
from PIL import Image

# Configuración inicial de la página
st.set_page_config(layout="wide", page_title="Generador y Clasificador de Imágenes")

# Título de la aplicación
st.title("Aplicación Web con Modelos de HuggingFace")

col1, col2 = st.columns(2)

# Sección 1: Generación de Imágenes
with col1:
    st.header("Generador de Imágenes")
    prompt = st.text_input("Describe la imagen que quieres generar:")#es para colocar un subtitulo
    if st.button("Generar Imagen"):
        if prompt:
            with st.spinner("Generando imagen..."):
                generated_image = generate_image(prompt)
                st.image(generated_image, caption="Imagen Generada", use_column_width=True)
        else:
            st.error("Por favor ingresa una descripción para generar la imagen.")

# Sección 2: Clasificación de Imágenes
with col2:
    st.header("Clasificador de Imágenes")
    uploaded_file = st.file_uploader("Sube una imagen para clasificarla", type=["jpg", "jpeg", "png"])#puede ser de esos 3 tipos, por ejemplo en wpp descargamos de .jpg
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Imagen Cargada", use_column_width=True)
        if st.button("Clasificar Imagen"):
            with st.spinner("Clasificando imagen..."):
                classification = classify_image(image)
                st.success(f"Clase Predicha: {classification}")