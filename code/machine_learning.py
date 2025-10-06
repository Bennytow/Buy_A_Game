# Importar las librerías necesarias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar el archivo CSV
def cargar_juegos(ruta_archivo: str):
    df = pd.read_csv(ruta_archivo)
    return df

# Seleccionar solo las columnas que nos interesan: ventas_NA (para predecir) y ventas_global (lo que queremos predecir)
def preparar_datos(df):
    X = df[['NA_Sales']]  # Esta es nuestra característica (lo que usamos para predecir)
    y = df['Global_Sales']  # Esta es nuestra etiqueta (lo que queremos predecir)
    return X, y

# Crear el modelo de regresión lineal
def crear_modelo(X, y):
    modelo = LinearRegression()  # Usamos regresión lineal, que es muy sencillo
    modelo.fit(X, y)  # Entrenamos el modelo con nuestros datos
    return modelo

# Hacer predicciones con el modelo entrenado
def hacer_predicciones(modelo, X_test):
    return modelo.predict(X_test)

# Evaluar el modelo
def evaluar_modelo(y_test, y_pred):
    # Evaluamos el modelo con el error cuadrado medio (es un tipo de medida que nos dice lo bien que está haciendo el modelo)
    error = mean_squared_error(y_test, y_pred)
    print(f"Error cuadrático medio: {error}")

# Función principal
def main():
    # Cargar los datos
    df = cargar_juegos('juegos.csv')  # Asegúrate de tener el archivo CSV con datos de juegos
    
    # Preparar los datos (separamos las características y la etiqueta)
    X, y = preparar_datos(df)

    # Dividir los datos en dos partes: una para entrenar el modelo y otra para probarlo
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Crear y entrenar el modelo
    modelo = crear_modelo(X_train, y_train)

    # Hacer predicciones sobre los datos de prueba
    y_pred = hacer_predicciones(modelo, X_test)

    # Evaluar el modelo con las predicciones
    evaluar_modelo(y_test, y_pred)

    # Mostrar algunas predicciones
    print(f"Primeras predicciones: {y_pred[:5]}")  # Mostrar las primeras 5 predicciones

if __name__ == '__main__':
    main()





