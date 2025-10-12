# *videojuegos bajo la lupa* (Buy A Game)
Integrantes:
- Benny Javed Gomez Ruiz
- Duvan Andres Alarcon Mora
- Duvan Felipe Leon Vallejo
- Carlos Mario Mazabel Mora
## INTRODUCCION
En este proyecto veremos la manera en que los videojuegos a lo largo de su historia han logrado grandes exitos, esto no solo a nivel local o nacional, lo vemos reflejado alrededor del mundo, hoy en día es muy complicado que alguien no conozca el termino vid3eojuego, gracias a ello han emergido empresas o franquicias como: Rockstar, Nintendo, Activision o Gameloft, sin embargo, siempre fue asi? que parametros debe cumplir un juego para entrar en la lista de posibles exitos? todo esto se hara bajo un analisis profundo de datos los cuales nos serviran como guia para responder estas preguntas y muchas mas
## Caracteristicas
- Predice ventas de videojuegos usando Mahcine Learning
- Se categoriza en datos como plataforma , genero y puntuacion de criticos
- Permite comparar resultados reales contra predicciones
- Entrenamiento y pruebas personalizables
- Estructura modular para facil mantenimiento
## Librerias Usadas
|Libreria|Descripcion|
|--------|-----------|
|**Pandas**|maneja y analiza datos en forma de tablas (hojas de exel o archivos csv) limpia los datos y los ordena facilmente|
|**Numpy**|trabaja con numeros, matrices y operaciones matematicas rapidas, es la base de la matematica en el machine learning (da promedios etc..)|
|**Scikit-learn**|proporciona algoritmos de Machine Learning (regresiones, predicciones etc..) es la base del modelo predictivo de ventas|
|**Matplotlib**|crea graficos y visualizaciones, muestra los resultados de la predicciones(ventas reales y estimadas)|
|**Joblib**|Sirve para guardar y cargar objetos de Python como modelos de MAchine Learning|
## prediccion de ventas de videojuegos
- Este proyecto utiliza modelos de Machine Learning en Python para predecir las ventas futuras de videojuegos.
El objetivo principal es identificar los factores clave que determinan el éxito comercial de un juego, considerando variables como género, plataforma, año de lanzamiento y la compañía desarrolladora.
El programa permite analizar patrones históricos de ventas y generar predicciones confiables para nuevos títulos, ofreciendo información valiosa para desarrolladores, analistas de mercado y entusiastas de la industria de los videojuegos.
---
## objetivo
- Analizar las principales variables que determinan el rendimiento comercial de un videojuego.  
- Entrenar un modelo predictivo que estime las ventas globales (`Global_Sales`).  
- Permitir ejecutar el modelo desde consola ingresando características del videojuego.
## dataset
-**Fuente:** [OpenDataBay](https://opendatabay.com/)  
-**Formato:** CSV (video_games_sales.csv)
**Variables principales:**
  -| Variable | Descripción |
  -|-----------|-------------|
  -| (Name) | Nombre del videojuego |
  -| (Platform) | Consola o sistema  |
  -| (Genre) | Género del juego |
  -| (Publisher) | Empresa desarrolladora |
  -| (Year) | Año de lanzamiento |
  -| (Global_Sales) | Ventas totales en millones de unidades |
 ----

 ## Futuras mejoras
 * Incluir interfaz Grafica
 * Hacer sistemas de Usuario (Login)
 * Agregar Base de datos
 * Crear una pagina de inicio mas atractiva

