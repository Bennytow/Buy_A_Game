#Importar pandas
import pandas as pd
#Cargar datos
def load_data(path: str):
    #Lee el documento csv, limpia los datos y retorna cache(Dataframe).
    # Lee el archivo CSV
    df = pd.read_csv(path)

    # Elimina filas completamente vacías
    df = df.dropna(how='all')

    # Elimina espacios extra en los nombres de las columnas
    df.columns = [c.strip() for c in df.columns]

    # Convierte la columna año a un numero
    if 'Year' in df.columns:
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

    # Convierte las columnas de ventas a float
    for col in ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)
#Retorna df
    return df
