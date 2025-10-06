#Esta funcion se encarga de organizar los datos de los juegos y subirlos a una lista separandolo por año, genero etc..
# importar joblib, no sé bien qué hace pero parece que sirve para cargar el modelo
import joblib
modelo = joblib.load('../models/modelo_entrenado.pkl')
#Funcion para hacer predicciones
def predicciones(X_nuevo):
    predicciones = modelo.predict(X_nuevo)
    return predicciones
def cargar_juegos(ruta_archivo:str)->list:
#Organizacio del archivo csv
#Rango,Nombre,Plataforma,Año,Genero,Puntuacion,Na_ventas,EU_ventas,Jp_ventas,Otras_ventas
#Rank,Name,Platform,Year,Genre,Publisher,NA_Sales,EU_Sales,JP_Sales,Other_Sales,Global_Sales
    juegos=[]
    archivo=open(ruta_archivo,'r')
    titulos=archivo.readline()
    print(titulos)
    informacion=archivo.readline()
    
    while len(informacion)>0:
        info=informacion.split(',')
        posicion=info[0]
        nombre=info[1]
        plataforma=info[2]
        anio=info[3]
        genero=info[4]
        editor=info[5]
        ventas_NA=info[6]
        ventas_EU=info[7]
        ventas_JP=info[8]
        ventas_X=info[9]
        ventas_global=info[10]
        l_juegos={'rango':rango,
                  'nombre':nombre,
                  'plataforma':plataforma,
                  'anio':anio,
                  'genero':genero,
                  'puntuacion':puntuacion,
                  'ventas_NA':ventas_NA,
                  'ventas_EU':ventas_EU,
                  'ventas_JP':ventas_JP,
                  'ventas_X':ventas_X,
                  'ventas_Global':ventas_global}
        juegos.append(l_juegos)
        
        info=archivo.readline()
    archivo.close()
    return juegos
#De aqui en adelante hare aalgunas funciones para mostrar al usuario un poco de organizacion
