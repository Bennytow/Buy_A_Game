#Esta funcion se encarga de organizar los datos de los juegos y subirlos a una lista
def cargar_juegos(ruta_archivo:str)->list:
#Organizacio del archivo csv
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
        ventas_NA=
        ventas_EU=
        ventas_JP=
        ventas_X=
        l_juegos={'plataforma':plataforma,
                         'nombre':nombre,
                         'plataforma':plataforma,
                         'anio':anio,
                         'genero':genero}
        juegos.append(l_canciones)
        
        info=archivo.readline()
    archivo.close()
    return juegos
