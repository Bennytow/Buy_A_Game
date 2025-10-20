import customtkinter as ctk
from tkinter import ttk, messagebox
import pandas as pd
from PIL import Image, ImageTk

# --- CONFIGURACIÓN GLOBAL DE ESTILO ---
ctk.set_appearance_mode("dark")   # "dark" o "light"
ctk.set_default_color_theme("blue")

# --- VENTANA PRINCIPAL ---
root = ctk.CTk()
root.title("Videojuegos Bajo Lupa")
root.geometry("1280x720")

# Fondo tipo “glassmorphism”
try:
    imagen_fondo = Image.open("image.jpg").resize((1920, 1080))
    fondo_tk = ImageTk.PhotoImage(imagen_fondo)

    fondo_label = ctk.CTkLabel(root, image=fondo_tk, text="")
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")

# Colores
PRIMARY_COLOR = "#00adb5"
SECONDARY_COLOR = "#222831"  # 🔹 Color secundario
TEXT_COLOR = "#C7C5B1"

# 🔹 Estilo para la tabla (solo añadido esto)
style = ttk.Style()
style.theme_use("default")
style.configure(
    "Treeview",
    background=SECONDARY_COLOR,
    fieldbackground=SECONDARY_COLOR,
    foreground=TEXT_COLOR,
    rowheight=25,
)
style.map(
    "Treeview",
    background=[("selected", PRIMARY_COLOR)]
)

# Título
label = ctk.CTkLabel(
    root,
    text="¿Compraras un juego o lo pondrás en el mercado?",
    font=("Segoe UI Semibold", 24),
    text_color=PRIMARY_COLOR,
)
label.pack(pady=20)

# Línea separadora
separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", pady=5)

# --- CARGAR DATASET ---
df = pd.read_csv("../data/dataset/vgsales.csv")

# --- FUNCIONES DE LÓGICA ---
def obtener_df_filtrado():
    plataforma = platform_var.get()
    genero = genre_var.get()
    df_filtrado = df.copy()
    if plataforma != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Platform"] == plataforma]
    if genero != "Todos":
        df_filtrado = df_filtrado[df_filtrado["Genre"] == genero]
    return df_filtrado

def filtrar_tabla():
    df_filtrado = obtener_df_filtrado()
    for i in tree.get_children():
        tree.delete(i)
    for _, row in df_filtrado.iterrows():
        tree.insert("", "end", values=list(row))

def mostrar_ventas_totales():
    df_filtrado = obtener_df_filtrado()
    total = df_filtrado["Global_Sales"].sum()
    messagebox.showinfo(
        "Ventas Globales (filtradas)",
        f"Según filtros seleccionados:\n{platform_var.get()} / {genre_var.get()}\n\nTotal global de ventas: ${total:.2f} millones"
    )

def predecir_tilin():
    ventana_pred = ctk.CTkToplevel(root)
    ventana_pred.title("Predicción de tu videojuego")
    ventana_pred.geometry("400x350")

    ctk.CTkLabel(
        ventana_pred,
        text="Ingresa los datos de tu videojuego",
        text_color=PRIMARY_COLOR,
        font=("Segoe UI Semibold", 14)
    ).pack(pady=15)

    genero_pred = ctk.StringVar(value="Todos")
    plataforma_pred = ctk.StringVar(value="Todos")

    ctk.CTkLabel(ventana_pred, text="Género:", text_color=TEXT_COLOR).pack()
    genre_menu_pred = ctk.CTkComboBox(
        ventana_pred, variable=genero_pred, values=genre_options, width=220
    )
    genre_menu_pred.pack(pady=5)

    ctk.CTkLabel(ventana_pred, text="Plataforma:", text_color=TEXT_COLOR).pack()
    platform_menu_pred = ctk.CTkComboBox(
        ventana_pred, variable=plataforma_pred, values=platform_options, width=220
    )
    platform_menu_pred.pack(pady=5)

    ctk.CTkLabel(ventana_pred, text="Ventas esperadas (en millones):", text_color=TEXT_COLOR).pack()
    ventas_entry = ctk.CTkEntry(ventana_pred, width=220)
    ventas_entry.pack(pady=5)

    def calcular_prediccion():
        genero = genero_pred.get()
        plataforma = plataforma_pred.get()
        try:
            ventas_esperadas = float(ventas_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa un número válido para las ventas.")
            return

        df_filtrado = df.copy()
        if genero != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Genre"] == genero]
        if plataforma != "Todos":
            df_filtrado = df_filtrado[df_filtrado["Platform"] == plataforma]

        if not df_filtrado.empty:
            promedio_ventas = df_filtrado["Global_Sales"].mean()
            diferencia = ventas_esperadas - promedio_ventas

            if diferencia > 0:
                resultado = f"Tu predicción es OPTIMISTA =)\nPodrías superar el promedio de ventas ({promedio_ventas:.2f} millones)."
            elif diferencia < 0:
                resultado = f"Tu predicción es CONSERVADORA\nPodrías vender menos que el promedio ({promedio_ventas:.2f} millones)."
            else:
                resultado = f"Tu predicción es EXACTA\nCoincide con el promedio del dataset."
        else:
            resultado = "No hay datos suficientes para esa combinación de género y plataforma."

        messagebox.showinfo(
            "Predicción de Ventas",
            f"Género: {genero}\nPlataforma: {plataforma}\n"
            f"Ventas esperadas: {ventas_esperadas:.2f} millones\n\n{resultado}"
        )

    ctk.CTkButton(ventana_pred, text="Predecir", command=calcular_prediccion).pack(pady=15)

# --- FILTROS ---
frame_filtros = ctk.CTkFrame(root, fg_color=("gray10", "gray20"))
frame_filtros.pack(pady=10)

platform_var = ctk.StringVar(value="Todos")
genre_var = ctk.StringVar(value="Todos")

platform_options = ["Todos"] + sorted(df["Platform"].dropna().unique().tolist())
genre_options = ["Todos"] + sorted(df["Genre"].dropna().unique().tolist())

ctk.CTkLabel(frame_filtros, text="Plataforma:", text_color=TEXT_COLOR).grid(row=0, column=0, padx=8)
platform_menu = ctk.CTkComboBox(frame_filtros, variable=platform_var, values=platform_options, width=150)
platform_menu.grid(row=0, column=1, padx=8)

ctk.CTkLabel(frame_filtros, text="Género:", text_color=TEXT_COLOR).grid(row=0, column=2, padx=8)
genre_menu = ctk.CTkComboBox(frame_filtros, variable=genre_var, values=genre_options, width=150)
genre_menu.grid(row=0, column=3, padx=8)

ctk.CTkButton(frame_filtros, text="Filtrar", command=filtrar_tabla).grid(row=0, column=4, padx=10)
ctk.CTkButton(frame_filtros, text="Ventas Globales", command=mostrar_ventas_totales).grid(row=0, column=5, padx=10)

ctk.CTkButton(root, text="Predecir tu juego", command=predecir_tilin).pack(pady=20)

# --- TABLA ---
frame_tabla = ctk.CTkFrame(root)
frame_tabla.pack(expand=True, fill="both")

scrollbar = ttk.Scrollbar(frame_tabla)
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

# Footer
footer = ctk.CTkLabel(
    root,
    text="Desarrollado por Benny Gomez — Andres Mora - Duvan Leon - Mario Mora Proyecto de predicción de videojuegos",
    text_color="#888",
    font=("Segoe UI", 9)
)
footer.pack(side="bottom", pady=10)

root.mainloop()
