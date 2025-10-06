# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Cargar el dataset
df = pd.read_csv('../data/dataset.csv')  # Asume que el dataset está en la carpeta 'data'

# Preprocesamiento básico
df = df.dropna()  # Eliminar valores nulos
df = pd.get_dummies(df, drop_first=True)  # Codificación de variables categóricas

# Separar características y etiqueta
X = df.drop('target', axis=1)  # Suponemos que 'target' es la columna a predecir
y = df['target']

# Dividir los datos en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo
modelo = LogisticRegression()

# Entrenar el modelo
modelo.fit(X_train, y_train)



