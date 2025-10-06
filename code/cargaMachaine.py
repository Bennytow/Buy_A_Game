#Esta funcion se encarga de organizar los datos de los juegos y subirlos a una lista separandolo por año, genero etc..
# importar joblib, no sé bien qué hace pero parece que sirve para cargar el modelo
import joblib
modelo = joblib.load('../models/modelo_entrenado.pkl')
#Funcion para hacer predicciones
def predicciones(X_nuevo):
    predicciones = modelo.predict(X_nuevo)
    return predicciones
def cargar_juegos(ruta_archivo:str)->list:
#Organizacio del archivo csv
#Rango,Nombre,Plataforma,Año,Genero,Puntuacion,Na_ventas,EU_ventas,Jp_ventas,Otras_ventas
