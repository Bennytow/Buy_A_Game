import customtkinter as ctk
from tkinter import ttk, messagebox
import joblib
import pandas as pd
from PIL import Image, ImageTk
import time
import pygame  
import matplotlib.pyplot as plt  # <- añadido para la gráfica

def mostrar_intro():
    pygame.mixer.init()
    try:
        pygame.mixer.Sound("intro_sound.wav").play()  
    except:
        print("No se encontró el archivo de sonido (intro_sound.wav). Se omitirá el sonido.")

    splash = ctk.CTk()
    splash.overrideredirect(True)
    splash.geometry("500x300+500+250")
    splash.configure(fg_color="black")

    try:
        lupa = ctk.CTkImage(light_image=Image.open("lupa.png"), size=(120, 120))
        label_img = ctk.CTkLabel(splash, image=lupa, text="")
        label_img.place(relx=0.5, rely=0.4, anchor="center")
    except:
        label_img = ctk.CTkLabel(splash, text="🔍", text_color="white", font=("Arial", 100))
        label_img.place(relx=0.5, rely=0.4, anchor="center")

    texto = ctk.CTkLabel(
        splash,
        text="Buy A Game\n Videojuegos bajo lupa",
        text_color="white",
        font=("Arial Black", 28)
    )
    texto.place(relx=0.5, rely=0.75, anchor="center")

    splash.update()

    for i in range(0, 11):
        splash.attributes("-alpha", i / 10)
        splash.update()
        time.sleep(0.1)

    time.sleep(1.5)

    for i in range(10, -1, -1):
        splash.attributes("-alpha", i / 10)
        splash.update()
        time.sleep(0.08)

    splash.destroy()

mostrar_intro()

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Videojuegos Bajo Lupa")
root.geometry("1280x720")
root.attributes('-alpha', 0.0)

try:
    imagen_fondo = Image.open("image.jpg").resize((1920, 1080))
    fondo_tk = ImageTk.PhotoImage(imagen_fondo)
    fondo_label = ctk.CTkLabel(root, image=fondo_tk, text="")
    fondo_label.place(x=0, y=0, relwidth=1, relheight=1)
except Exception as e:
    print(f"No se pudo cargar la imagen de fondo: {e}")

PRIMARY_COLOR = "#CA72D4"
SECONDARY_COLOR = "#241924"
TEXT_COLOR = "#B3AAB3"

style = ttk.Style()
style.theme_use("default")
style.configure(
    "Treeview",
    background=SECONDARY_COLOR,
    fieldbackground=SECONDARY_COLOR,
    foreground=TEXT_COLOR,
    rowheight=25,
)
style.map("Treeview", background=[("selected", PRIMARY_COLOR)])

label = ctk.CTkLabel(
    root,
    text="¿Compraras un juego o lo pondrás en el mercado?",
    font=("Segoe UI Semibold", 24),
    text_color=PRIMARY_COLOR,
)
label.pack(pady=20)

separator = ttk.Separator(root, orient="horizontal")
separator.pack(fill="x", pady=5)

df = pd.read_csv("../data/dataset/vgsales.csv")

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

    # Agrupar por plataforma y género
    df_grafica = df_filtrado.groupby(["Platform", "Genre"])["Global_Sales"].sum().unstack(fill_value=0)

    # Graficar
    df_grafica.plot(kind="bar", figsize=(12,6), stacked=True, colormap="viridis")
    plt.title(f"Ventas globales por plataforma y género\nFiltros: {platform_var.get()} / {genre_var.get()}")
    plt.ylabel("Ventas (millones)")
    plt.xlabel("Plataforma")
    plt.xticks(rotation=45)
    plt.legend(title="Género")
    plt.tight_layout()
    plt.show()

def predecir_tilin():
    import joblib
    import pandas as pd   

    modelo = joblib.load("./models/modelo_entrenado.pkl")

    ventana_pred = ctk.CTkToplevel(root)
    ventana_pred.title("Predicción de tu videojuego")
    ventana_pred.geometry("400x350")

    ctk.CTkLabel(
        ventana_pred,
        text="Predcie las posibles ventas de tu videojuego!!",
        text_color=PRIMARY_COLOR,
        font=("Segoe UI Semibold", 14)
    ).pack(pady=15)

    genero_pred = ctk.StringVar(value="")
    plataforma_pred = ctk.StringVar(value="")
    año_pred = ctk.StringVar(value="")
    puntuacion_pred = ctk.StringVar(value="7.5")

    # entradas del user  

    ctk.CTkLabel(ventana_pred, text="Genero:", text_color=TEXT_COLOR).pack()
    ctk.CTkComboBox(ventana_pred, variable=genero_pred, values=genre_options, width=220).pack(pady=5)
    
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

footer = ctk.CTkLabel(
    root,
    text="Desarrollado por Benny Gomez — Andres Mora - Duvan Leon - Mario Mora Proyecto de predicción de videojuegos",
    text_color="#888",
    font=("Segoe UI", 9)
)
footer.pack(side="bottom", pady=10)

def fade_in(window, alpha=0.0):
    if alpha < 1.0:
        alpha += 0.05
        window.attributes('-alpha', alpha)
        window.after(50, lambda: fade_in(window, alpha))
    else:
        window.attributes('-alpha', 1.0)

fade_in(root)
root.mainloop()

