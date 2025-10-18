import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Interfaz en ventana
root = tk.Tk()
root.configure(bg="#b30000")
root.title("Videojuegos Bajo Lupa")
root.geometry("1920x1080")  # Tamaño de la ventana

# Etiqueta de bienvenida
label = tk.Label(root, text="¿Comprarás un juego? Solo observa ;)", font=("Arial", 18))
label.pack(pady=10)

# Cargar el dataset
df = pd.read_csv("../data/dataset/vgsales.csv")

# Función para obtener el DataFrame filtrado
def obtener_df_filtrado():
    """Devuelve un DataFrame filtrado según la plataforma y género seleccionados."""
    plataforma = platform_var.get()
    genero = genre_var.get()
    df_filtrado = df.copy()
    if plataforma != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Platform"] == plataforma]
    if genero != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Genre"] == genero]
    return df_filtrado

# Función para filtrar y mostrar la tabla
def filtrar_tabla():
    df_filtrado = obtener_df_filtrado()
    # Limpiar tabla
    for i in tree.get_children():
        tree.delete(i)
    # Insertar filas filtradas
    for _, row in df_filtrado.iterrows():
        tree.insert("", "end", values=list(row))

# Función para mostrar ventas globales totales según los filtros
def mostrar_ventas_totales():
    df_filtrado = obtener_df_filtrado()
    total = df_filtrado["Global_Sales"].sum()
    messagebox.showinfo(
        "Ventas Globales (filtradas)",
        f"Según filtros seleccionados:\n{platform_var.get()} / {genre_var.get()}\n\nTotal global de ventas: ${total:.2f} millones"
    )

# Filtros principales
frame_filtros = tk.Frame(root)
frame_filtros.pack(pady=10)

platform_var = tk.StringVar(value="Todos")
genre_var = tk.StringVar(value="Todos")

platform_options = ["Todos"] + sorted(df["Platform"].dropna().unique().tolist())
genre_options = ["Todos"] + sorted(df["Genre"].dropna().unique().tolist())

tk.Label(frame_filtros, text="Plataforma:").grid(row=0, column=0, padx=5)
platform_menu = ttk.Combobox(frame_filtros, textvariable=platform_var, values=platform_options, state="readonly")
platform_menu.grid(row=0, column=1, padx=5)

tk.Label(frame_filtros, text="Género:").grid(row=0, column=2, padx=5)
genre_menu = ttk.Combobox(frame_filtros, textvariable=genre_var, values=genre_options, state="readonly")
genre_menu.grid(row=0, column=3, padx=5)

tk.Button(frame_filtros, text="Filtrar", command=filtrar_tabla).grid(row=0, column=4, padx=5)
tk.Button(frame_filtros, text="Ventas Globales", command=mostrar_ventas_totales).grid(row=0, column=5, padx=5)

# Tabla con scroll
frame_tabla = tk.Frame(root)
frame_tabla.pack(expand=True, fill="both")

scrollbar = tk.Scrollbar(frame_tabla)
scrollbar.pack(side="right", fill="y")

tree = ttk.Treeview(frame_tabla, yscrollcommand=scrollbar.set)
tree["columns"] = list(df.columns)
tree["show"] = "headings"

scrollbar.config(command=tree.yview)

# Encabezados para orden
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")  # Ajusta ancho

# Insertar datos iniciales
for _, row in df.iterrows():
    tree.insert("", "end", values=list(row))

tree.pack(expand=True, fill="both")

# Ejecutar la ventana
root.mainloop()

