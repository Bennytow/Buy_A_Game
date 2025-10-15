#Importamos librerias
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib
import os

# Cargar datos
df = pd.read_csv('data/dataset/vgsales.csv')

# Preparar datos
X = df[['NA_Sales']]
y = df['Global_Sales']

# Dividir datos
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entrenar modelo
modelo = LinearRegression()
modelo.fit(X_train, y_train)

# Evaluar modelo
y_pred = modelo.predict(X_test)
error = mean_squared_error(y_test, y_pred)
print(f"Error cuadrático medio: {error}")

# Guardar modelo
ruta_modelo = os.path.join('models', 'modelo_entrenado.pkl')
joblib.dump(modelo, ruta_modelo)
print(f"Modelo guardado en {ruta_modelo}")

