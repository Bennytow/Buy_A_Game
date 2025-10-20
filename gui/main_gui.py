import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
from PIL import Image, ImageTk
import os

# -----------------------------------
# VENTANA PRINCIPAL
# -----------------------------------
root = tk.Tk()
root.title("Videojuegos Bajo Lupa")
root.geometry("1000x600")

# Colores principales
PRIMARY_COLOR = "#CCCCCC"  # gris claro
SECONDARY_COLOR = "#333333"  # gris oscuro

# -----------------------------------
# FONDO CON IMAGEN (opcional)
# -----------------------------------
ruta_imagen = "../data/background.jpg"  # cambia a tu ruta real
if os.path.exists(ruta_imagen):
    bg_image = Image.open(ruta_imagen)
    bg_image = bg_image.resize((1000, 600))
    bg_photo = ImageTk.PhotoImage(bg_image)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)
else:
    root.configure(bg=SECONDARY_COLOR)

# -----------------------------------
# ETIQUETA PRINCIPAL
# -----------------------------------
label = tk.Label(
    root,
    text="¿Comprarás un juego? Solo observa ;)",
    font=("Arial", 18, "bold"),
    fg=PRIMARY_COLOR,
    bg=SECONDARY_COLOR,
)
label.pack(pady=10)

# -----------------------------------
# CARGAR DATASET
# -----------------------------------
df = pd.read_csv("../data/dataset/vgsales.csv")

# -----------------------------------
# FUNCIONES
# -----------------------------------
def filtrar_tabla():
    plataforma = platform_var.get()
    genero = genre_var.get()
    df_filtrado = df.copy()
    if plataforma != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Platform"] == plataforma]
    if genero != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Genre"] == genero]

    # limpiar tabla
    for i in tree.get_children():
        tree.delete(i)

    # insertar filas filtradas
    for _, row in df_filtrado.iterrows():
        tree.insert("", "end", values=list(row))


def mostrar_ventas_totales():
    plataforma = platform_var.get()
    genero = genre_var.get()

    df_filtrado = df.copy()
    if plataforma != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Platform"] == plataforma]
    if genero != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Genre"] == genero]

    total = df_filtrado["Global_Sales"].sum()
    messagebox.showinfo("Ventas Globales Totales", f"${total:.2f} millones")


def predecir_ventas_nacionales():
    genero = genre_var.get()

    if genero == "Todos":
        messagebox.showwarning("Atención", "Por favor selecciona un género.")
        return

    df_genre = df[df["Genre"] == genero]
    if df_genre.empty:
        messagebox.showinfo("Resultado", "No hay datos para ese género.")
        return

    prediccion = df_genre["NA_Sales"].mean()
    messagebox.showinfo(
        "Predicción de Ventas Nacionales",
        f"Basado en el género '{genero}', se espera un promedio de ventas de {prediccion:.2f} millones en Norteamérica.",
    )


# -----------------------------------
# FILTROS
# -----------------------------------
frame_filtros = tk.Frame(root, bg=SECONDARY_COLOR)
frame_filtros.pack(pady=10)

platform_var = tk.StringVar(value="Todos")
genre_var = tk.StringVar(value="Todos")

platform_options = ["Todos"] + sorted(df["Platform"].dropna().unique().tolist())
genre_options = ["Todos"] + sorted(df["Genre"].dropna().unique().tolist())

tk.Label(frame_filtros, text="Plataforma:", bg=SECONDARY_COLOR, fg=PRIMARY_COLOR).grid(row=0, column=0, padx=5)
platform_menu = ttk.Combobox(frame_filtros, textvariable=platform_var, values=platform_options, state="readonly")
platform_menu.grid(row=0, column=1, padx=5)

tk.Label(frame_filtros, text="Género:", bg=SECONDARY_COLOR, fg=PRIMARY_COLOR).grid(row=0, column=2, padx=5)
genre_menu = ttk.Combobox(frame_filtros, textvariable=genre_var, values=genre_options, state="readonly")
genre_menu.grid(row=0, column=3, padx=5)

tk.Button(frame_filtros, text="Filtrar", command=filtrar_tabla).grid(row=0, column=4, padx=5)
tk.Button(frame_filtros, text="Ventas Globales", command=mostrar_ventas_totales).grid(row=0, column=5, padx=5)
tk.Button(frame_filtros, text="Predecir Ventas Nacionales", command=predecir_ventas_nacionales).grid(row=0, column=6, padx=5)

# -----------------------------------
# TABLA CON SCROLL
# -----------------------------------
frame_tabla = tk.Frame(root)
frame_tabla.pack(expand=True, fill="both")

scrollbar = tk.Scrollbar(frame_tabla)
scrollbar.pack(side="right", fill="y")

tree = ttk.Treeview(frame_tabla, yscrollcommand=scrollbar.set)
tree["columns"] = list(df.columns)
tree["show"] = "headings"

scrollbar.config(command=tree.yview)

for col in df.columns:
    tree.heading(col, text=col)
    tree.column(col, width=100, anchor="center")

for _, row in df.iterrows():
    tree.insert("", "end", values=list(row))

tree.pack(expand=True, fill="both")

# -----------------------------------
# MAINLOOP
# -----------------------------------
root.mainloop()
