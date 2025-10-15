#Use pandas para limpiar el dataset
import pandas as pd#manipulacion de datos
import numpy as np#operaciones numericas
import os
# Crear nueva carpeta para el dataset ya organizado
os.makedirs("data/clean", exist_ok=True)#crear carpeta
 
# Guardar la ruta del archivo original
ruta_archivo = input("Por favor ingrese el nombre del archivo CSV con los juegos: ")
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

# Filtrar años (Lo filtre en un rango para que haya juegos mas o menos actualizados)
datos_limpios = datos_limpios[(datos_limpios['Year'] >= 1970) & (datos_limpios['Year'] <= 2025)]
#Rango de 1970 a 2025

# Limpiar columna de texto
columnas_texto = ['Platform', 'Genre', 'Publisher']
for columna in columnas_texto:
    datos_limpios[columna] = datos_limpios[columna].astype(str).str.strip()

# Convierte las ventas globales a entero
datos_limpios['Global_Sales'] = pd.to_numeric(datos_limpios['Global_Sales'], errors='coerce').fillna(0)
print("Validacion de datos")
print("Filas finales:", len(datos_limpios))
print("Duplicados después de limpiar:", datos_limpios.duplicated().sum())
print("Valores nulos restantes:\n", datos_limpios.isna().sum())
#Guardar el datsaset ya limpio
ruta_salida = "data/clean/vgsales_limpio.csv"
datos_limpios.to_csv(ruta_salida, index=False, encoding="utf-8")
print(f"\nArchivo limpio guardado en: {ruta_salida}")
#Reporte
filas_originales = len(datos_originales)
filas_finales = len(datos_limpios)

reporte_limpieza = f"""
# Reporte de Limpieza del Dataset
- Filas originales: {filas_originales}
- Filas finales: {filas_finales}
"""

with open("data/clean/README_limpieza.md", "w", encoding="utf-8") as archivo_reporte:
    archivo_reporte.write(reporte_limpieza)
