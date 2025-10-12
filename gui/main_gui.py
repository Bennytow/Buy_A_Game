import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd

# -------------------
# Ventana principal
# -------------------
root = tk.Tk()
root.title("Video Game Sales")
root.geometry("1000x600")  # Tamaño de la ventana

# Etiqueta de bienvenida
label = tk.Label(root, text="Bienvenido a Video Game Sales!", font=("Arial", 18))
label.pack(pady=20)

# -------------------
# Leer dataset
# -------------------
df = pd.read_csv("../data/video_game_sales.csv")  # Ajusta la ruta según tu CSV

# -------------------
# Tabla para mostrar datos
# -------------------
tree = ttk.Treeview(root)
tree["columns"] = list(df.columns)
tree["show"] = "headings"

# Encabezados
for col in df.columns:
    tree.heading(col, text=col)

# Filas
for _, row in df.iterrows():
    tree.insert("", "end", values=list(row))

tree.pack(expand=True, fill="both")

# -------------------
# Ejecutar ventana
# -------------------
root.mainloop()

