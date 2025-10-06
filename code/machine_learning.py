# Importamos cosas para que funcione todo
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Abrimos archivo de los juegos, que es como una caja llena de cosas
def cargar_juegos(ruta_archivo: str):
    df = pd.read_csv(ruta_archivo)  # Leemos el archivo, mas o menos
    return df

# Seleccionamos lo que queremos de los datos, osea, lo importante
def preparar_datos(df):
    X = df[['NA_Sales']]  # Esto es lo que usamos pa' adivinar
    y = df['Global_Sales']  # Esto es lo que queremos predecir
    return X, y

# Hacemos magia con un modelo de esos para que aprenda
def crear_modelo(X, y):
    modelo = LinearRegression()  # Es una linea, no tiene mucha ciencia
    modelo.fit(X, y)  # Lo entrenamos y listo
    return modelo

# Ahora hacemos que el modelo diga cosas
def hacer_predicciones(modelo, X_test):
    return modelo.predict(X_test)

# Vemos si el modelo acierta o se equivoca mucho
def evaluar_modelo(y_test, y_pred):
    error = mean_squared_error(y_test, y_pred)  # Calculamos el error, que se ve medio raro
    print(f"Error cuadratico medio: {error}")  # Mostramos el numero raro

# Todo esto lo hacemos aqui
def main():
    df = cargar_juegos('juegos.csv')  # Abres el archivo que tienes por ahi
    X, y = preparar_datos(df)  # Seleccionamos que usar para adivinar
    
    # Partimos los datos en dos partes: una para entrenar y otra para probar
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Creamos el modelo y lo entrenamos, asi de facil
    modelo = crear_modelo(X_train, y_train)
    
    # Le preguntamos al modelo sobre los datos que no vio
    y_pred = hacer_predicciones(modelo, X_test)
    
    # Evaluamos si se equivoco mucho o poco
    evaluar_modelo(y_test, y_pred)
    
    # Miramos unas predicciones pa' ver que tal
    print(f"Primeras predicciones: {y_pred[:5]}")  # Vemos las primeras predicciones

if __name__ == '__main__':
    main()





