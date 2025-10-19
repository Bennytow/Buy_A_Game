import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# Interfaz en ventana
root = tk.Tk()
# Estilo general
root.configure(bg="#1b1f2a")

style = ttk.Style()
style.theme_use("clam")
PRIMARY_COLOR = "#00adb5"
SECONDARY_COLOR = "#393e46"
BACKGROUND = "#222831"
TEXT_COLOR = "#eeeeee"
HOVER_COLOR = "#007b83"

style.configure("Treeview",
    background=SECONDARY_COLOR,
    foreground=TEXT_COLOR,
    fieldbackground=SECONDARY_COLOR,
    rowheight=28,
    font=("Segoe UI", 10)
)

style.configure("Treeview.Heading",
    background="#0078d7",
    foreground="white",
    font=("Times New Roman", 10, "bold")
)
style.configure("Treeview.Heading",
    background=PRIMARY_COLOR,
    foreground="white",
    font=("Segoe UI", 11, "bold")
)

style.map("Treeview",
    background=[("selected", HOVER_COLOR)],
    foreground=[("selected", "white")]
)
root.title("Videojuegos Bajo Lupa")
root.geometry("1280x720")  # Tamaño de la ventana

# Etiqueta de bienvenida
label = tk.Label(
    root,
    text="¿Comprarás un juego? Solo observa ",
    font=("Segoe UI Semibold", 22),
    bg=BACKGROUND,
    fg=PRIMARY_COLOR,
)
label.pack(pady=20)
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", pady=5)


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
def predecir_tilin():
    mensaje = "Ventana de prediccion"
    messagebox.showinfo("Prediccion de tu videojuego")

# Filtros principales
frame_filtros = tk.Frame(root)
frame_filtros.pack(pady=10)

platform_var = tk.StringVar(value="Todos")
genre_var = tk.StringVar(value="Todos")

platform_options = ["Todos"] + sorted(df["Platform"].dropna().unique().tolist())
genre_options = ["Todos"] + sorted(df["Genre"].dropna().unique().tolist())

tk.Label(frame_filtros, text="Plataforma:", bg=BACKGROUND, fg=TEXT_COLOR, font=("Segoe UI", 11)).grid(row=0, column=0, padx=8)
platform_menu = ttk.Combobox(frame_filtros, textvariable=platform_var, values=platform_options, state="readonly", width=18)
platform_menu.grid(row=0, column=1, padx=8)

tk.Label(frame_filtros, text="Género:", bg=BACKGROUND, fg=TEXT_COLOR, font=("Segoe UI", 11)).grid(row=0, column=2, padx=8)
genre_menu = ttk.Combobox(frame_filtros, textvariable=genre_var, values=genre_options, state="readonly", width=18)
genre_menu.grid(row=0, column=3, padx=8)

ttk.Button(frame_filtros, text=" Filtrar", command=filtrar_tabla).grid(row=0, column=4, padx=10)
ttk.Button(frame_filtros, text=" Ventas Globales", command=mostrar_ventas_totales).grid(row=0, column=5, padx=10)

boton = tk.Button(root, text=("Presioname"), command=predecir_tilin)
boton.pack(pady=20)

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
footer = tk.Label(
    root,
    text="Desarrollado por Benny Gomez-Andres Alarcon-Carlos Mazabel Duván León — Proyecto de predicción de precios de videojuegos ",
    bg=BACKGROUND,
    fg="#888",
    font=("Segoe UI", 9)
)
footer.pack(side="bottom", pady=10)

# Ejecutar la ventana
root.mainloop() 