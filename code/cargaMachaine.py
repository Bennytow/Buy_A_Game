#Utilisaremos joblib para el modelo
import joblib
modelo = joblib.load('../models/modelo_entrenado.pkl')
#Funcion para hacer predicciones
def predicciones(X_nuevo):
    predicciones = modelo.predict(X_nuevo)
    return predicciones
#Organizacio del archivo csv
#Rango,Nombre,Plataforma,Año,Genero,Puntuacion,Na_ventas,EU_ventas,Jp_ventas,Otras_ventas
