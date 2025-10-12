import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

#interfaz en ventana
root = tk.Tk()
root.title("Videojuegos Bajo Lupa")
root.geometry("1000x600")  # Tamaño de la ventana

# etiqueta de bienvenida
label = tk.Label(root, text="Compraras un juego?, solo observa ;)", font=("Arial", 18))
label.pack(pady=10)

#aqui se lee el dataset
df = pd.read_csv("../data/dataset/vgsales.csv")  

#funciones principales
def filtrar_tabla():
    plataforma = platform_var.get()
    genero = genre_var.get()
    # filtrar dataframe
    df_filtrado = df.copy()
    if plataforma != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Platform"] == plataforma]
    if genero != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Genre"] == genero]
    
    # limpiar tabla
    for i in tree.get_children():
        tree.delete(i)
    # Insertar filas filtradas
    for _, row in df_filtrado.iterrows():
        tree.insert("", "end", values=list(row))

def mostrar_ventas_totales():
    total = df["Global_Sales"].sum()
    messagebox.showinfo("Ventas Globales Totales", f"${total:.2f} millones")

# -------------------
# Filtros
# -------------------
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

# -------------------
# Tabla con scroll
# -------------------
frame_tabla = tk.Frame(root)
frame_tabla.pack(expand=True, fill="both")

scrollbar = tk.Scrollbar(frame_tabla)
scrollbar.pack(side="right", fill="y")

tree = ttk.Treeview(frame_tabla, yscrollcommand=scrollbar.set)
tree["columns"] = list(df.columns)
tree["show"] = "headings"

scrollbar.config(command=tree.yview)

# Encabezados
for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")  # Ajusta ancho

# Insertar datos
for _, row in df.iterrows():
    tree.insert("", "end", values=list(row))

tree.pack(expand=True, fill="both")

# -------------------
# Ejecutar ventana
# -------------------
root.mainloop()
