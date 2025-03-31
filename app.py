import streamlit as st
import pandas as pd
import plotly.express as px


# Cargar datos
@st.cache_data
def load_data():
    df = pd.read_csv("vehicles_us.csv")
    df["manufacturer"] = df["model"].str.split().str[0]  # Extraer fabricante
    return df


# Histograma del kilometraje
def show_histogram():
    car_data = load_data()
    st.header("Distribución del kilometraje de los vehículos")
    fig = px.histogram(car_data, x="odometer",
                       labels={"odometer": "Kilometraje"},
                       color_discrete_sequence=["#8FBC8F"])  # 008B8B
    st.plotly_chart(fig, use_container_width=True)


# Diagrama de dispersión entre kilometraje y precio
def show_scatter_plot():
    car_data = load_data()
    st.header("Relación entre kilometraje y precio")
    fig = px.scatter(car_data, x="odometer", y="price",
                     labels={"odometer": "Kilometraje", "price": "Precio"},
                     color="price", opacity=0.6,
                     color_continuous_scale="Viridis")
    st.plotly_chart(fig, use_container_width=True)


# Tipos de vehículos por fabricante
def plot_vehicle_types():
    df = load_data()
    st.header("Tipos de vehículos por fabricante")
    fig = px.bar(df, x="manufacturer", color="type", barmode="stack",
                 labels={"manufacturer": "Fabricante"},
                 color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig, use_container_width=True)


# Histograma de condición por modelo
def plot_condition_vs_year():
    df = load_data()
    st.header("Histograma de condición vs año del modelo")
    fig = px.histogram(df, x="model_year", color="condition", barmode="stack",
                       labels={"model_year": "Año"},
                       color_discrete_sequence=px.colors.qualitative.Pastel1)
    st.plotly_chart(fig, use_container_width=True)


# Interfaz
def main():
    st.title("Análisis de Datos de :blue[Ventas de Vehículos]")

    if st.checkbox("Mostrar histograma del kilometraje"):
        show_histogram()

    if st.checkbox("Mostrar diagrama de dispersión entre kilometraje y precio"):
        show_scatter_plot()

    if st.checkbox("Mostrar tipos de vehículos por fabricante"):
        plot_vehicle_types()

    if st.checkbox("Mostrar histograma de condición vs año del modelo"):
        plot_condition_vs_year()


if __name__ == "__main__":
    main()
