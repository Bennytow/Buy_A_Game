import csv

def cargar_juegos(ruta_archivo: str) -> list:
    juegos = []
    
    # Abriendo el archivo CSV y leyendo su contenido
    with open(ruta_archivo, 'r', newline='', encoding='utf-8') as archivo:
        lector = csv.DictReader(archivo)  # Esto automáticamente usa las cabeceras del archivo como claves

        # Iteramos sobre cada fila del archivo CSV
        for fila in lector:
            # Convertimos las ventas a valores numéricos (float) si no están vacías, si están vacías se asigna 0
            ventas_NA = float(fila['NA_Sales']) if fila['NA_Sales'] else 0.0
            ventas_EU = float(fila['EU_Sales']) if fila['EU_Sales'] else 0.0
            ventas_JP = float(fila['JP_Sales']) if fila['JP_Sales'] else 0.0
            ventas_X = float(fila['Other_Sales']) if fila['Other_Sales'] else 0.0
            ventas_global = float(fila['Global_Sales']) if fila['Global_Sales'] else 0.0

            # Creamos el diccionario para este juego
            l_juego = {
                'nombre': fila['Name'],
                'plataforma': fila['Platform'],
                'anio': fila['Year'],
                'genero': fila['Genre'],
                'editor': fila['Publisher'],
                'ventas_NA': ventas_NA,
                'ventas_EU': ventas_EU,
                'ventas_JP': ventas_JP,
                'ventas_X': ventas_X,
                'ventas_global': ventas_global
            }
            
            # Añadimos el juego a la lista de juegos
            juegos.append(l_juego)
    
    return juegos
