# importar joblib, no sé bien qué hace pero parece que sirve para cargar el modelo
import joblib
modelo = joblib.load('../models/modelo_entrenado.pkl')
#Funcion para hacer predicciones
def predicciones(X_nuevo):
    predicciones = modelo.predict(X_nuevo)
    return predicciones
