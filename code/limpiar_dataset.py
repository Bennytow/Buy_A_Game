#!/usr/bin/env python3
"""
code/limpiar_dataset.py
Versión robusta del limpiador de vgsales.csv

Uso:
    python code/limpiar_dataset.py --input data/raw/vgsales.csv --output data/clean/vgsales_limpio.csv
Si no se pasa input, usa 'data/raw/vgsales.csv' por defecto.
"""

from pathlib import Path
import pandas as pd
import argparse
from datetime import datetime

def parse_args():
    parser = argparse.ArgumentParser(description="Limpieza del dataset vgsales")
    parser.add_argument("--input", "-i", type=str, default=str(Path("data") / "raw" / "vgsales.csv"),
                        help="Ruta al CSV original (por defecto: data/raw/vgsales.csv)")
    parser.add_argument("--output", "-o", type=str, default=str(Path("data") / "clean" / "vgsales_limpio.csv"),
                        help="Ruta salida CSV limpio (por defecto: data/clean/vgsales_limpio.csv)")
    parser.add_argument("--min-year", type=int, default=1970,
                        help="Año mínimo aceptado (por defecto: 1970)")
    parser.add_argument("--max-year", type=int, default=None,
                        help="Año máximo aceptado (por defecto: año actual)")
    return parser.parse_args()

def safe_read_csv(path: Path) -> pd.DataFrame:
    # Intenta leer con utf-8 y si falla intenta latin1
    try:
        return pd.read_csv(path)
    except UnicodeDecodeError:
        return pd.read_csv(path, encoding="latin1")

def resumen_nulos(df: pd.DataFrame) -> pd.DataFrame:
    nulos = df.isna().sum()
    pct = (nulos / len(df) * 100).round(2)
    return pd.DataFrame({"nulos": nulos, "porcentaje": pct})

def limpiar_dataframe(df: pd.DataFrame, min_year: int, max_year: int):
    stats = {}
    antes = len(df)
    stats['filas_iniciales'] = antes

    # drop exact duplicates
    df = df.drop_duplicates()
    stats['drop_duplicates'] = antes - len(df)
    antes = len(df)

    # Name: eliminar filas sin nombre
    if 'Name' in df.columns:
        df = df.loc[df['Name'].notna()]
        df = df.loc[df['Name'].str.strip() != ""]
    stats['sin_name'] = antes - len(df)
    antes = len(df)

    # Year: convertir a numérico, eliminar inválidos, convertir a int
    if 'Year' in df.columns:
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce')
        n_year_invalid = df['Year'].isna().sum()
        df = df.dropna(subset=['Year'])
        df.loc[:, 'Year'] = df['Year'].astype(int)
        stats['year_invalid'] = n_year_invalid

        # Filtrar por rango
        df = df.loc[(df['Year'] >= min_year) & (df['Year'] <= max_year)]
        stats['outside_year_range'] = antes - len(df) - stats.get('year_invalid', 0)
        antes = len(df)

    # Columnas de texto: strip y normalizar NaN
    text_cols = ['Platform', 'Genre', 'Publisher']
    for c in text_cols:
        if c in df.columns:
            df.loc[:, c] = df[c].astype(str).str.strip().replace({'nan': pd.NA})
    
    # Global_Sales: numérico, NaN -> 0.0
    if 'Global_Sales' in df.columns:
        df.loc[:, 'Global_Sales'] = pd.to_numeric(df['Global_Sales'], errors='coerce').fillna(0.0)

    # Duplicados basados en Name+Year (opcional)
    if set(['Name', 'Year']).issubset(df.columns):
        dup_name_year = df.duplicated(subset=['Name', 'Year']).sum()
        df = df.drop_duplicates(subset=['Name', 'Year'])
        stats['dup_name_year'] = dup_name_year

    stats['filas_finales'] = len(df)
    return df, stats

def save_report(output_dir: Path, stats: dict, df_before: pd.DataFrame):
    now = datetime.now().isoformat(timespec='seconds')
    report_lines = [
        "# Reporte de Limpieza del Dataset",
        f"- Fecha: {now}",
        f"- Filas originales: {stats.get('filas_iniciales')}",
        f"- Filas finales: {stats.get('filas_finales')}",
        f"- Eliminadas por duplicados exactos: {stats.get('drop_duplicates')}",
        f"- Eliminadas por Name vacío: {stats.get('sin_name')}",
        f"- Eliminadas por Year inválido: {stats.get('year_invalid')}",
        f"- Eliminadas por fuera de rango Year: {stats.get('outside_year_range')}",
        f"- Eliminadas por duplicados Name+Year: {stats.get('dup_name_year', 0)}",
        "",
        "## Nulos antes de la limpieza (conteo y %):",
        df_before.isna().sum().to_string(),
        "",
        "## Resumen: nulos (%) antes:",
        resumen_nulos(df_before).to_markdown()
    ]
    out = output_dir / "README_limpieza.md"
    output_dir.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(report_lines), encoding="utf-8")
    return out

def main():
    args = parse_args()
    input_path = Path(args.input)
    output_path = Path(args.output)
    max_year = args.max_year or datetime.now().year

    if not input_path.exists():
        print(f"[ERROR] No se encontró el archivo: {input_path}")
        return

    df = safe_read_csv(input_path)
    df_before = df.copy()
    print("Dimensiones iniciales:", df.shape)
    print("Nulos por columna (inicial):")
    print(resumen_nulos(df))

    df_clean, stats = limpiar_dataframe(df, args.min_year, max_year)

    # Guardar csv limpio
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df_clean.to_csv(output_path, index=False, float_format="%.6f", encoding="utf-8")
    print(f"CSV limpio guardado en: {output_path}")

    # Guardar reporte
    report_file = save_report(output_path.parent, stats, df_before)
    print(f"Reporte de limpieza guardado en: {report_file}")

    # Mensaje final
    print("=== RESUMEN FINAL ===")
    for k, v in stats.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()

