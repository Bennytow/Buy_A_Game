# Buy A Game
## *videojuegos bajo la lupa* 
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

Esta carpeta contiene un análisis completo de las ventas globales de videojuegos, realizado con **Python**, **Pandas** y **Matplotlib**.  
El propósito del estudio es identificar tendencias en la industria a lo largo de los años, los géneros más populares y las plataformas con mayores ventas acumuladas.

El script principal es [`analisis_vgsales.py`](graficas/analisis_vgsales.py), el cual toma los datos del archivo [`vgsales.csv`](graficas/vgsales.csv), procesa la información y genera las siguientes gráficas:

---

### Ventas Globales por Año
Representa la evolución de las ventas de videojuegos a nivel mundial a lo largo del tiempo.

![Ventas Globales Por Año](graficas/Ventas%20Globales%20Por%20Año.png)

---

### Ventas Globales por Género
Muestra qué tipos de videojuegos (acción, deportes, rol, etc.) registran mayores ventas globales.

![Ventas Globales Por Genero](graficas/Ventas%20Globales%20Por%20Genero.png)

---

### Top 15 Plataformas con Mayores Ventas Globales
Presenta las 15 plataformas de videojuegos con mayor volumen de ventas globales en la historia.

![Top 15 Plataformas con Mayores Ventas Globales](graficas/Top%2015%20Plataformas%20con%20Mayores%20Ventas%20Globales.png)

---

### Herramientas utilizadas
- **Python 3**
- **Pandas** → para manejo y análisis de datos
- **Matplotlib** → para creación de gráficos
- **Google Colab / Visual Studio Code** → entorno de desarrollo

---

### Conclusiones generales
- Las ventas globales presentan picos en determinados años, coincidiendo con el auge de consolas específicas.  
- Los géneros de acción y deportes dominan el mercado.  
- Las plataformas históricamente más exitosas en ventas han sido aquellas con una amplia base de usuarios y soporte de desarrolladores.

---

> Todos los resultados se encuentran dentro de la carpeta [`graficas/`](graficas/).  
> Este análisis forma parte del proyecto colaborativo del grupo, enfocado en estudiar las tendencias del mercado global de videojuegos.



