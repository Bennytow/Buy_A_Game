"""
Uso:
    python billboard.py --input data/raw/vgsales.csv --output data/clean/vgsales_limpio.csv
    python billboard.py                      # Pedirá interactivo el nombre/ruta del CSV si no existe

Descripción:
    Script para limpiar el dataset vgsales. Si no se pasa --input o el archivo no existe,
    el programa preguntará interactivamente por la ruta del CSV. Los nombres de variables
    y ejemplos están alineados con tus scripts anteriores: `ruta_archivo`, `ruta_salida`,
    `datos_originales`, `datos_limpios`.
"""

from pathlib import Path
import pandas as pd
import argparse
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="Limpieza del dataset vgsales")
    # Si no se proporciona --input/-i, se usará el comportamiento interactivo
    parser.add_argument("--input", "-i", type=str, default=None,
                        help="Ruta al CSV original (si no se pasa, se pedirá por input o se usará el valor por defecto)")
    parser.add_argument("--output", "-o", type=str, default=None,
                        help="Ruta salida CSV limpio (si no se pasa, se guardará en data/clean/vgsales_limpio.csv por defecto)")
    parser.add_argument("--min-year", type=int, default=1970,
                        help="Año mínimo aceptado (por defecto: 1970)")
    parser.add_argument("--max-year", type=int, default=None,
                        help="Año máximo aceptado (por defecto: año actual)")
    return parser.parse_args()

def safe_read_csv(path: Path) -> pd.DataFrame:
    """Leer CSV de forma segura intentando varias codificaciones.

    Parámetros:
        path: Path a leer
    Devuelve:
        DataFrame con los datos
    """
    # Intenta leer con utf-8 y si falla intenta latin1
    try:
        return pd.read_csv(path)
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1")

def resumen_nulos(datos: pd.DataFrame) -> pd.DataFrame:
    nulos = datos.isna().sum()
    pct = (nulos / len(datos) * 100).round(2)
    return pd.DataFrame({"nulos": nulos, "porcentaje": pct})

def limpiar_dataframe(datos: pd.DataFrame, min_year: int, max_year: int):
    estadisticas = {}
    antes = len(datos)
    estadisticas['filas_iniciales'] = antes

    # eliminar duplicados exactos
    datos = datos.drop_duplicates()
    estadisticas['drop_duplicates'] = antes - len(datos)
    antes = len(datos)

    # Name: eliminar filas sin nombre
    if 'Name' in datos.columns:
        datos = datos.loc[datos['Name'].notna()]
        datos = datos.loc[datos['Name'].str.strip() != ""]
    estadisticas['sin_name'] = antes - len(datos)
    antes = len(datos)

    # Year: convertir a numérico, eliminar inválidos, convertir a int
    if 'Year' in datos.columns:
        datos['Year'] = pd.to_numeric(datos['Year'], errors='coerce')
        n_year_invalid = datos['Year'].isna().sum()
        datos = datos.dropna(subset=['Year'])
        datos.loc[:, 'Year'] = datos['Year'].astype(int)
        estadisticas['year_invalid'] = n_year_invalid

        # Filtrar por rango
        datos = datos.loc[(datos['Year'] >= min_year) & (datos['Year'] <= max_year)]
        estadisticas['outside_year_range'] = antes - len(datos) - estadisticas.get('year_invalid', 0)
        antes = len(datos)

    # Columnas de texto: strip y normalizar NaN
    columnas_texto = ['Platform', 'Genre', 'Publisher']
    for c in columnas_texto:
        if c in datos.columns:
            datos.loc[:, c] = datos[c].astype(str).str.strip().replace({'nan': pd.NA})
    
    # Global_Sales: numérico, NaN -> 0.0
    if 'Global_Sales' in datos.columns:
        datos.loc[:, 'Global_Sales'] = pd.to_numeric(datos['Global_Sales'], errors='coerce').fillna(0.0)

    # Duplicados basados en Name+Year (opcional)
    if set(['Name', 'Year']).issubset(datos.columns):
        duplicados_nombre_anyo = datos.duplicated(subset=['Name', 'Year']).sum()
        datos = datos.drop_duplicates(subset=['Name', 'Year'])
        estadisticas['dup_name_year'] = duplicados_nombre_anyo

    estadisticas['filas_finales'] = len(datos)
    return datos, estadisticas

def save_report(ruta_salida_dir: Path, estadisticas: dict, datos_antes: pd.DataFrame):
    now = datetime.now().isoformat(timespec='seconds')
    report_lines = [
        "# Reporte de Limpieza del Dataset",
        f"- Fecha: {now}",
        f"- Filas originales: {estadisticas.get('filas_iniciales')}",
        f"- Filas finales: {estadisticas.get('filas_finales')}",
        f"- Eliminadas por duplicados exactos: {estadisticas.get('drop_duplicates')}",
        f"- Eliminadas por Name vacío: {estadisticas.get('sin_name')}",
        f"- Eliminadas por Year inválido: {estadisticas.get('year_invalid')}",
        f"- Eliminadas por fuera de rango Year: {estadisticas.get('outside_year_range')}",
        f"- Eliminadas por duplicados Name+Year: {estadisticas.get('dup_name_year', 0)}",
        "",
        "## Nulos antes de la limpieza (conteo y %):",
        datos_antes.isna().sum().to_string(),
        "",
        "## Resumen: nulos (%) antes:",
        resumen_nulos(datos_antes).to_markdown()
    ]
    out = ruta_salida_dir / "README_limpieza.md"
    ruta_salida_dir.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(report_lines), encoding="utf-8")
    return out

def main():
    args = parse_args()
    # Valores por defecto (concordantes con tus scripts)
    DEFAULT_INPUT = Path(r"c:\Users\duvan\Buy_A_Game\Buy_A_Game\data\dataset\vgsales.csv")
    DEFAULT_OUTPUT_DIR = Path(r"c:\Users\duvan\Buy_A_Game\Buy_A_Game\data\clean")
    DEFAULT_OUTPUT = DEFAULT_OUTPUT_DIR / "vgsales_limpio.csv"

    # Resolver input: usar arg, si es None preguntar, si no existe ofrecer pedir la ruta
    if args.input:
        ruta_archivo = Path(args.input)
    else:
        # Preguntar al usuario
        entrada = input(f"Por favor ingrese el nombre o ruta del archivo CSV (enter para usar '{DEFAULT_INPUT}'): ").strip()
        ruta_archivo = Path(entrada) if entrada else DEFAULT_INPUT

    # Si no existe, permitir reintentos
    while not ruta_archivo.exists():
        respuesta = input(f"El archivo '{ruta_archivo}' no existe. Desea ingresar otra ruta? (s/n): ").strip().lower()
        if respuesta in ('s', 'si'):
            entrada = input("Ingrese la ruta completa al CSV: ").strip()
            ruta_archivo = Path(entrada)
            continue
        else:
            print("Cancelado por el usuario. Saliendo.")
            return

    # Resolver output: usar arg, si es None usar default
    if args.output:
        ruta_salida = Path(args.output)
    else:
        ruta_salida = DEFAULT_OUTPUT

    max_year = args.max_year or datetime.now().year

    # Leer y trabajar con nombres de variables que usaste en tus scripts
    datos_originales = safe_read_csv(ruta_archivo)
    datos_antes = datos_originales.copy()
    print("Dimensiones iniciales:", datos_originales.shape)
    print("Nulos por columna (inicial):")
    print(resumen_nulos(datos_originales))

    # limpiar_dataframe devuelve datos_limpios y estadisticas
    datos_limpios, estadisticas = limpiar_dataframe(datos_originales, args.min_year, max_year)

    # Guardar csv limpio
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    datos_limpios.to_csv(ruta_salida, index=False, float_format="%.6f", encoding="utf-8")
    print(f"CSV limpio guardado en: {ruta_salida}")

    # Guardar reporte
    report_file = save_report(ruta_salida.parent, estadisticas, datos_antes)
    print(f"Reporte de limpieza guardado en: {report_file}")

    # Mensaje final
    print("=== RESUMEN FINAL ===")
    for k, v in estadisticas.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()

