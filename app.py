import streamlit as st

st.title("Convertidor a Mayúsculas")

# Caja de texto de entrada
texto_usuario = st.text_input("Escribe tu texto aquí:", "")

# Procesar el texto
texto_mayusculas = texto_usuario.upper()

# Mostrar el texto procesado en otra caja de texto (deshabilitada para que sea solo de salida)
st.text_input("Texto procesado (Mayúsculas):", value=texto_mayusculas, disabled=True)
