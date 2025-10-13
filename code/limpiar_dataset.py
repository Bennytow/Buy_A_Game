#Esta vez las librerias son pandas
import pandas as pd
import numpy as np
import os
# Crear nueva carpeta para el dataset ya organizado
os.makedirs("data/clean", exist_ok=True)

# Guardar la ruta del archivo original
ruta_archivo = "data/vgsales.csv"

# Leer datos
datos_originales = pd.read_csv(ruta_archivo, encoding="utf-8")
# Cuenta los valores nulos y los muestra en pantalla
valores_nulos = datos_originales.isna().sum()
print("\nValores nulos por columna:\n", valores_nulos)

# Cuenta valores nulos y los muestra en pantalla
duplicados = datos_originales.duplicated().sum()
print("\nNúmero de filas duplicadas:", duplicados)
#Esta variable es para modificar los valores sin cambiar el datset original
datos_limpios = datos_originales.copy()
#Aqui elimine valores duplicados
datos_limpios = datos_limpios.drop_duplicates()

# Elimine filas sin noombre :v
datos_limpios = datos_limpios[~datos_limpios['Name'].isna()]
datos_limpios = datos_limpios[datos_limpios['Name'].str.strip() != ""]

# Si aparece aalgun error con el año lo elimina
datos_limpios['Year'] = pd.to_numeric(datos_limpios['Year'], errors='coerce')
print("Antes de limpiar, valores nulos en 'Year':", datos_limpios['Year'].isna().sum())

# Eliminar filas sin año válido
datos_limpios = datos_limpios.dropna(subset=['Year'])

# Convertir los años a enteros
datos_limpios['Year'] = datos_limpios['Year'].astype(int)

# Filtrar años dentro de un rango lógico
datos_limpios = datos_limpios[(datos_limpios['Year'] >= 1970) & (datos_limpios['Year'] <= 2025)]
print("📅 Se corrigieron los años inválidos.")

# 3.4 Limpiar columnas de texto
columnas_texto = ['Platform', 'Genre', 'Publisher']
for columna in columnas_texto:
    datos_limpios[columna] = datos_limpios[columna].astype(str).str.strip()
print("🧾 Se limpiaron las columnas de texto (espacios eliminados).")

# 3.5 Convertir Global_Sales a número
datos_limpios['Global_Sales'] = pd.to_numeric(datos_limpios['Global_Sales'], errors='coerce').fillna(0)
print("💰 Se convirtieron los valores de ventas a números.")

# ===============================================================
# 4️⃣ VALIDACIÓN FINAL
# ===============================================================
print("\n✅ Validación final del dataset limpio:\n")
print("Filas finales:", len(datos_limpios))
print("Duplicados después de limpiar:", datos_limpios.duplicated().sum())
print("Valores nulos restantes:\n", datos_limpios.isna().sum())

# ===============================================================
# 5️⃣ GUARDAR EL NUEVO DATASET
# ===============================================================
ruta_salida = "data/clean/vgsales_limpio.csv"
datos_limpios.to_csv(ruta_salida, index=False, encoding="utf-8")
print(f"\n📁 Archivo limpio guardado en: {ruta_salida}")

# ===============================================================
# 6️⃣ CREAR UN REPORTE DE LIMPIEZA
# ===============================================================
filas_originales = len(datos_originales)
filas_finales = len(datos_limpios)

reporte_limpieza = f"""
# 🧹 Reporte de Limpieza del Dataset

**Archivo original:** data/vgsales.csv  
**Archivo limpio:** data/clean/vgsales_limpio.csv

### Cambios realizados:
1. Se eliminaron {duplicados} filas duplicadas.
2. Se eliminaron filas sin nombre de juego.
3. Se corrigieron y eliminaron valores nulos en la columna 'Year'.
4. Se eliminaron años fuera del rango 1970-2025.
5. Se limpiaron espacios en las columnas Platform, Genre y Publisher.
6. Se convirtieron las ventas globales a valores numéricos.

### Resumen:
- Filas originales: {filas_originales}
- Filas finales: {filas_finales}
"""

with open("data/clean/README_limpieza.md", "w", encoding="utf-8") as archivo_reporte:
    archivo_reporte.write(reporte_limpieza)

print("\n📝 Reporte de limpieza creado correctamente en data/clean/README_limpieza.md")
print("\n🚀 Proceso completado con éxito.")
