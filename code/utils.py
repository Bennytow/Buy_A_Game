import pandas as pd

def load_data(path: str):
    """
    Lee el CSV, limpia los datos y retorna el DataFrame.
    """
    # Lee el archivo CSV
    df = pd.read_csv(path)

    # Elimina filas completamente vacías
    df = df.dropna(how='all')

    # Elimina espacios extra en los nombres de las columnas
    df.columns = [c.strip() for c in df.columns]

    # Convierte la columna 'Year' a numérica si existe
    if 'Year' in df.columns:
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')

    # Convierte las columnas de ventas a float
    for col in ['NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0.0)

    return df
