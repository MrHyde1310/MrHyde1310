import streamlit as st
st.title('PRS PRUEBA')
st.header('Visualización de Datos')
st.subheader('Gráfico de barras')

data = [10, 20, 30, 40, 50]
st.bar_chart(data)

st.subheader('Tabla de Datos')
st.write(data)


