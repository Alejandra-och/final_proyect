import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header("Visualización de datos para anuncios de venta en Vehículos en EE.UU.")
# Mostrar tabla de datos
st.dataframe(car_data)

hist_button = st.button('Construir histograma')  # crear un botón


if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer",
                       title='Cantidad de vehiculos ofrecidos según su kilometraje(millas)')
    # agregar etiquetas a los ejes
    fig.update_xaxes(title_text='Kilometraje (millas)')
    fig.update_yaxes(title_text='Cantidad de vehículos')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)


scatter_button = st.button(
    'Construir diagrama de dispersión')  # crear un botón


if scatter_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Creación de un grafico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # crear un gráfico de dispersión
    fig = px.scatter(car_data, x="odometer", y="price",
                     title='Relación entre el precio y el kilometraje(millas)')
    # agregar etiquetas a los ejes
    fig.update_xaxes(title_text='Kilometraje (millas)')
    fig.update_yaxes(title_text='Precio (USD)')

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
