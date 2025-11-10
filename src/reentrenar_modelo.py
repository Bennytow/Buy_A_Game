# ============================================
# Reentrenar modelo predictivo (usando NA_Sales como entrada)
# ============================================

import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib
import json
import os

# ===============================
# 1️⃣ Cargar los datos
# ===============================
# Carga el archivo CSV desde la carpeta "data/dataset"
data_path = os.path.join("..", "data", "dataset", "clean", "vgsales_limpio.csv")
df = pd.read_csv(data_path)

print("🧾 Columnas encontradas:", df.columns.tolist())

# ===============================
# 2️⃣ Preparar las variables
# ===============================
# Variables independientes (entradas)
# Usamos NA_Sales como una de las variables de entrada
X = df[['Platform', 'Genre', 'Year', 'NA_Sales']]

# Convertir columnas categóricas a numéricas (one-hot encoding)
X = pd.get_dummies(X, drop_first=True)

# Variable dependiente (salida)
# 👉 Cambia 'Global_Sales' si quieres predecir otra variable (por ejemplo 'EU_Sales')
y = df['Global_Sales']

# ===============================
# 3️⃣ Entrenar el modelo
# ===============================
modelo = LinearRegression()
modelo.fit(X, y)

# ===============================
# 4️⃣ Guardar modelo y columnas
# ===============================
# Crear carpeta "models" si no existe
os.makedirs(os.path.join("..", "models"), exist_ok=True)

# Guardar modelo entrenado
modelo_path = os.path.join("..", "models", "modelo_entrenado.pkl")
joblib.dump(modelo, modelo_path)

# Guardar columnas usadas (para usar en predicciones futuras)
columnas_path = os.path.join("..", "models", "columnas_modelo.json")
with open(columnas_path, "w") as f:
    json.dump(list(X.columns), f)

print("✅ Modelo reentrenado y guardado correctamente.")
print(f"📂 Archivo guardado en: {modelo_path}")
print(f"🧩 Columnas usadas: {len(X.columns)} columnas")

