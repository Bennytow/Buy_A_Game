# Importamos libreriaas
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Abrimos archivo de los juegos (datacenter limpio).
def cargar_juegos(ruta_archivo: str):
    df = pd.read_csv(ruta_archivo)  # Leemos el archivo, mas o menos
    return df

# Seleccionamos lo que queremos de los datos, osea, lo importante
def preparar_datos(df):
    X = df[['NA_Sales']]  # Esto es lo que usamos pa' adivinar
    y = df['Global_Sales']  # Esto es lo que queremos predecir
    return X, y

# Creamos el modelo
def crear_modelo(X, y):
    modelo = LinearRegression()  # Es una linea, no tiene mucha ciencia
    modelo.fit(X, y)  # Lo entrenamos y listo
    return modelo

# Funcion para las predicciones.
def hacer_predicciones(modelo, X_test):
    return modelo.predict(X_test)

# Vemos aciertos y errores.
def evaluar_modelo(y_test, y_pred):
    error = mean_squared_error(y_test, y_pred)  # Calculamos el error, que se ve medio raro
    print(f"Error cuadratico medio: {error}")  # Mostramos el numero raro

# Esta funcion ya reune todas para asi organizarlas y guardarlas en variables
def main():
    df = cargar_juegos('juegos.csv')  # Abre el archivo
    X, y = preparar_datos(df)  # Seleccionamos que usar
    
    # Partimos los datos en dos partes: una para entrenar y otra para probar
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Creamos el modelo y lo entrenamos.
    modelo = crear_modelo(X_train, y_train)
    
    # Le preguntamos al modelo sobre los datos que no vio.
    y_pred = hacer_predicciones(modelo, X_test)
    
    # Evaluamos si se equivoco mucho o poco
    evaluar_modelo(y_test, y_pred)
    
    # Miramos unas predicciones para ver que tal
    print(f"Primeras predicciones: {y_pred[:5]}")  # Vemos las primeras predicciones

if __name__ == '__main__':
    main()





