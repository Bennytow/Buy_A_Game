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

if __name__ == "__main__":
    # Cargar nuevos datos desde un CSV
    datos_nuevos = pd.read_csv("../data/nuevos_videojuegos.csv")

    # Seleccionar solo las columnas que el modelo necesita
    columnas = ["Rango", "Nombre", "Plataforma", "Año", "Genero",
                "Puntuacion", "Na_ventas", "EU_ventas", "Jp_ventas", "Otras_ventas"]
    X_nuevo = datos_nuevos[columnas]

    # Obtener las predicciones
    resultados = predicciones(X_nuevo)

    # Mostrar o guardar las predicciones
    datos_nuevos["Prediccion"] = resultados
    print(datos_nuevos[["Nombre", "Prediccion"]])

