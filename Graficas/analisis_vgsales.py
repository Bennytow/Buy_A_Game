#ANALISIS DE VENTAS DE VIDEOJUEGOS

#Importar librerías necesarias
import pandas as pd #libreria para manipulacion de datos
import matplotlib.pyplot as plt #subbiblioteca "pyplot" para generar graficas

#Cargar el archivo CSV
data = pd.read_csv("vgsales.csv")#funcion de pandas para devolver una tabla

#Mostrar las primeras filas para verificar
print("Vista previa de los datos:")
print(data.head())

#Eliminar filas con valores faltantes en la columna 'Year'
data = data.dropna(subset=['Year'])
#Convertir el año a tipo entero
data['Year'] = data['Year'].astype(int)

#GRÁFICA: Ventas por Año
ventas_por_año = data.groupby('Year')['Global_Sales'].sum()

plt.figure(figsize=(10, 5))
ventas_por_año.plot(kind='bar', color='skyblue')
plt.title("Ventas Globales por Año (millones de copias)")
plt.xlabel("Año de lanzamiento")
plt.ylabel("Ventas Globales (millones)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#GRÁFICA: Ventas por Género
ventas_por_genero = data.groupby('Genre')['Global_Sales'].sum().sort_values(ascending=False)

plt.figure(figsize=(10, 5))
ventas_por_genero.plot(kind='bar', color='orange')
plt.title("Ventas Globales por Género")
plt.xlabel("Género")
plt.ylabel("Ventas Globales (millones)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#GRÁFICA: Ventas por Plataforma
ventas_por_plataforma = data.groupby('Platform')['Global_Sales'].sum().sort_values(ascending=False).head(15)

plt.figure(figsize=(10, 5))
ventas_por_plataforma.plot(kind='bar', color='green')
plt.title("Top 15 Plataformas con Mayores Ventas Globales")
plt.xlabel("Plataforma")
plt.ylabel("Ventas Globales (millones)")
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

#RESUMEN FINAL
print("=== RESUMEN GENERAL ===")
print("Años analizados:", data['Year'].min(), "hasta", data['Year'].max())
print("Total de géneros analizados:", data['Genre'].nunique())
print("Total de plataformas analizadas:", data['Platform'].nunique())
print("Ventas globales totales:", round(data['Global_Sales'].sum(), 2), "millones de copias")

print("Análisis completado con éxito ")
