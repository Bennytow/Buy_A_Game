#Importamos librerias
import os
import joblib
import pandas as pd

# Carga del modelo entrenado
ruta_modelo = os.path.join(os.path.dirname(__file__), '..', 'models', 'modelo_entrenado.pkl')
modelo = joblib.load(ruta_modelo)

# Función para cargar los juegos desde el CSV
def cargar_juegos(ruta_archivo: str):
    df = pd.read_csv(ruta_archivo)
    return df.to_dict(orient='records')

# Función para hacer predicciones con el modelo cargado
def predicciones(X_nuevo):
    return modelo.predict(X_nuevo)
