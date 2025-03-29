# Proyecto Sprint 7

Esta página web es una herramienta interactiva de análisis de datos enfocada en la venta de vehículos de Estados Unidos. El análisis se realiza a través de diferentes dinámicas con Plotly.

Cuenta con gráficos interactivos que permiten el análisis de los datos, donde se puede visualizar:

- La distribución del kilometraje de los vehículos
- La relación entre el precio y el kilometraje
- La distribución del modelo según la marca
- El estado de los autos en función del año de fabricación.

Es ideal para compradores o vendedores que deseen entender mejor el mercado, así como para analistas interesados en tendencias de precios y características de los vehículos.

[Proyecto][def]

**DUDA**: al realizar la app de la moneda, tuve problemas en la parte de 'Render', en uno de los chats mencionaron lo siguiente:

config.toml
The config.toml is not necessary and it even causes problems, sinse it changes the default port streamlit uses and in some computers, some ports (like 10000) could be blocked, so it's not possible to easily validate if the app is working. I would just delete that section.

Estuve trabajando en el desarrollo del proyecto sin discho directorio, pero antes de subirlo, intenté agregrar el archivo como nos lo mencionan en las indicaciones del proyecto, pero al agregarlo la app ya no funcionaba, por ende, decidí quitar este directorio.

[def]: https://vehicle-project-qj6f.onrender.com