# Utilizaremos joblib para cargar el modelo
import joblib
import pandas as pd

# Cargar el modelo entrenado
modelo = joblib.load('../models/modelo_entrenado.pkl')

# Función para hacer predicciones
def predicciones(X_nuevo):
    """
    Recibe un DataFrame o lista con las mismas columnas que el modelo espera.
    Retorna las predicciones.
    """
    pred = modelo.predict(X_nuevo)
    return pred

