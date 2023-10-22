import streamlit as st

st.title('Mi Dashboard Streamlit')

# Campo de entrada para rutas de texto
ruta = st.text_input('Ingrese una ruta de texto', '/ruta/ejemplo')

st.write('Ruta ingresada:', ruta)
