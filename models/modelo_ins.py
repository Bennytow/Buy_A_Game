import joblib
import pandas as pd

# === 1️⃣ Cargar el modelo ===
ruta_modelo = "../models/modelo_entrenado.pkl"

print("🔍 Cargando modelo desde:", ruta_modelo)
modelo = joblib.load(ruta_modelo)

print("\n✅ MODELO CARGADO CORRECTAMENTE")
print("Tipo de modelo:", type(modelo))

# === 2️⃣ Ver atributos comunes ===
print("\n--- ATRIBUTOS DISPONIBLES ---")
print(dir(modelo))

# === 3️⃣ Ver columnas esperadas ===
try:
    print("\n📋 Columnas esperadas (feature_names_in_):")
    print(modelo.feature_names_in_)
except AttributeError:
    print("\n⚠️ Este modelo no tiene atributo 'feature_names_in_'.")

# === 4️⃣ Si es un pipeline, mostrar sus pasos ===
if hasattr(modelo, "steps"):
    print("\n🧩 Pipeline detectado. Pasos:")
    for nombre, paso in modelo.steps:
        print(f"  - {nombre}: {type(paso)}")

    # Intentar detectar preprocesador
    try:
        pre = modelo.named_steps["preprocessor"]
        print("\n🧰 Preprocesador encontrado:", type(pre))

        if hasattr(pre, "transformers_"):
            print("\nTransformadores dentro del preprocesador:")
            for nombre, trans, cols in pre.transformers_:
                print(f"  - {nombre}: {type(trans)} columnas={cols}")

            for nombre, trans, cols in pre.transformers_:
                if hasattr(trans, "get_feature_names_out"):
                    print(f"\n✨ Columnas generadas por {nombre}:")
                    print(trans.get_feature_names_out(cols))
    except Exception as e:
        print("\n⚠️ No se encontró un preprocesador o no se pudo acceder:", e)

# === 5️⃣ Predicción de prueba ===
print("\n--- PRUEBA DE PREDICCIÓN ---")

# 🔹 Usa las columnas correctas con las que reentrenaste tu modelo
X_test = pd.DataFrame({
    'Platform': ['PS4'],
    'Genre': ['Action'],
    'Year': [2015],
    'NA_Sales': [2.5]  # ✅ esta reemplaza a Score
})

print("Datos de prueba:")
print(X_test)

# === 6️⃣ Intento de predicción ===
try:
    # Transformar a One-Hot Encoding para coincidir con el modelo
    X_enc = pd.get_dummies(X_test, drop_first=True)

    # Cargar columnas del modelo para reordenar correctamente
    import json
    with open("../models/columnas_modelo.json", "r") as f:
        columnas = json.load(f)

    # Reordenar columnas según el modelo entrenado
    X_enc = X_enc.reindex(columns=columnas, fill_value=0)

    # Hacer predicción
    pred = modelo.predict(X_enc)
    print("\n✅ Predicción exitosa:", pred)
except Exception as e:
    print("\n❌ Error al predecir:", e)

print("\n🧾 Fin de la inspección del modelo.")
