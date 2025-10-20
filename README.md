# Buy A Game
## *Videojuegos bajo la lupa* 
Integrantes:
- Benny Javed Gomez Ruiz
- Duvan Andres Alarcon Mora
- Duvan Felipe Leon Vallejo
- Carlos Mario Mazabel Mora
## INTRODUCCIÓN
En este proyecto veremos la manera en que los videojuegos a lo largo de su historia han logrado grandes exitos, esto no solo a nivel local o nacional, lo vemos reflejado alrededor del mundo, hoy en día es muy complicado que alguien no conozca el termino videojuego, gracias a ello han emergido empresas o franquicias como: Rockstar, Nintendo, Activision o Gameloft, sin embargo, ¿Siempre fue asi? ¿Que parámetros debe cumplir un juego para entrar en la lista de posibles exitos? Todo esto se hara bajo un analisis profundo de datos los cuales nos serviran como guia para responder estas preguntas y muchas más.
## Caracteristicas
- Predice ventas de videojuegos usando Mahcine Learning
- Se categoriza en datos como plataforma , genero y puntuacion de criticos
- Permite comparar resultados reales contra predicciones
- Entrenamiento y pruebas personalizables
- Estructura modular para facil mantenimiento
## Librerias Usadas
|Libreria|Descripcion|
|--------|-----------|
|**Pandas**|  Maneja y analiza datos en forma de tablas (hojas de exel o archivos csv) limpia los datos y los ordena facilmente|
|**Numpy**|  Trabaja con numeros, matrices y operaciones matematicas rapidas, es la base de la matematica en el machine learning (da promedios etc..)|
|**Scikit-learn**|  Proporciona algoritmos de Machine Learning (regresiones, predicciones etc..) es la base del modelo predictivo de ventas|
|**Matplotlib**|  Crea graficos y visualizaciones, muestra los resultados de la predicciones(ventas reales y estimadas)|
|**Joblib**|  Sirve para guardar y cargar objetos de Python como modelos de MAchine Learning|
## Predicción de ventas de videojuegos
- Este proyecto utiliza modelos de Machine Learning en Python para predecir las ventas futuras de videojuegos.
El objetivo principal es identificar los factores clave que determinan el éxito comercial de un juego, considerando variables como género, plataforma, año de lanzamiento y la compañía desarrolladora.
El programa permite analizar patrones históricos de ventas y generar predicciones confiables para nuevos títulos, ofreciendo información valiosa para desarrolladores, analistas de mercado y entusiastas de la industria de los videojuegos.
---
## Objetivo
- Analizar las principales variables que determinan el rendimiento comercial de un videojuego.  
- Entrenar un modelo predictivo que estime las ventas globales (`Global_Sales`).  
- Permitir ejecutar el modelo desde consola ingresando características del videojuego.
## Dataset
-**Fuente:** [OpenDataBay](https://opendatabay.com/)  
-**Formato:** CSV (vgsales.csv)
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
 * Incluir interfaz Grafica(hecha:))
 * Hacer sistemas de Usuario (Login.)
 * Agregar Base de datos.
 * Crear una pagina de inicio mas atractiva
## Análisis de Ventas Globales de Videojuegos

  Esta carpeta contiene un analisis completo de las ventas globales de videojuegos, realizado con **Python**, **Pandas** y **Matplotlib**.  
El propósito del estudio es identificar tendencias en la industria a lo largo de los años, los géneros más populares y las plataformas con mayores ventas acumuladas.

El script principal es [`analisis_vgsales.py`](Graficas/analisis_vgsales.py), el cual toma los datos del archivo [`vgsales.csv`](Graficas/vgsales.csv), procesa la información y genera las siguientes gráficas:

---

### Ventas Globales por Año
  Representa la evolución de las ventas de videojuegos a nivel mundial a lo largo del tiempo.

![Ventas Globales Por Año](Graficas/Ventas%20Globales%20Por%20Año.png)

---

### Ventas Globales por Género
Muestra qué tipos de videojuegos (acción, deportes, rol, etc.) registran mayores ventas globales.

![Ventas Globales Por Genero](Graficas/Ventas%20Globales%20Por%20Genero.png)

---

### Top 15 Plataformas con Mayores Ventas Globales
Presenta las 15 plataformas de videojuegos con mayor volumen de ventas globales en la historia.

![Top 15 Plataformas con Mayores Ventas Globales](Graficas/Top%2015%20Plataformas%20con%20Mayores%20Ventas%20Globales.png)

---
# Entrenamiento del Modelo de Predicción de Ventas

## Objetivo
  Entrenar un modelo de **Regresión Lineal** que prediga las ventas globales de videojuegos (`Global_Sales`)
en función de las ventas por región (`NA_Sales`, `EU_Sales`, `JP_Sales`, `Other_Sales`).

---

## Proceso

1. **Carga del dataset limpio:**
   - Se utiliza el archivo `data/clean/vgsales_limpio.csv`.
   - Contiene las columnas necesarias sin valores nulos ni duplicados.

2. **Preparación de datos:**
   - Variables independientes: ventas por región.
   - Variable dependiente: ventas globales.

3. **División de datos:**
   - 80% de los datos se usa para entrenar el modelo.
   - 20% se reserva para probar la precisión del modelo.

4. **Entrenamiento:**
   - Se


### Herramientas utilizadas
- **Python 3**
- **Pandas** para manejo y análisis de datos
- **Matplotlib**  creación de gráficos
- **Google Colab / Visual Studio Code** entorno de desarrollo

---

## Bibliografia
* https://youtube.com/playlist?list=PL7HAy5R0ehQXb2aFKOKyeCMequxyb5jzJ&si=hnI6TGuzGHxyOLrG (explicacion de tkinter (libreria))
* https://youtube.com/playlist?list=PLg9145ptuAij_8zYgMeqwOV8ABwRYLuR3&si=jfRHMPP70IqYzsBJ (como usar numpy & pandas (libreria))
* https://www.youtube.com/watch?v=cTu74xMkolg (como incluir imagenes en tkinter)
* https://www.youtube.com/watch?v=Z1RJmh_OqeA (tkinter)
* https://www.youtube.com/watch?v=YXPyB4XeYLA (GUI)
* https://docs.python.org/3/
* https://freesound.org/people/nomentero/sounds/727926/ (sonido usado en el programa)
* https://www.uhdpaper.com/2025/02/4295c-sunset-moon-synthwave-night.html?m=0#google_vignette (imagen BACKGROUND bg)
* https://www.kaggle.com/ (datacenter principal)
* https://stackoverflow.com/questions/78237438/python-customtkinter-and-matplotlib?utm_source=chatgpt.com (referencia para usar customtkinter y matplotlib)
* https://pythonprogramming.net/how-to-embed-matplotlib-graph-tkinter-gui/?utm_source=chatgpt.com (como usar matplotlib)
* https://www.geeksforgeeks.org/python/how-to-embed-matplotlib-charts-in-tkinter-gui/
* https://www.deepl.com/es/translator (traductor usado para entender cada web o video)
