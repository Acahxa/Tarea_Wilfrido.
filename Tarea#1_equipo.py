import tkinter as tk
from tkinter import messagebox

def calcular():
    try:
        compra = float(entry_compra.get())
        color = entry_color.get().lower()

        if color == "roja":
            descuento = compra * 0.40
        elif color == "amarilla":
            descuento = compra * 0.25
        elif color == "blanca":
            descuento = 0
        else:
            messagebox.showerror("Error", "Color no válido")
            return

        total_pagar = compra - descuento

        resultado.config(
            text=f"Descuento: ${descuento:.2f}\nTotal a pagar: ${total_pagar:.2f}"
        )

    except ValueError:
        messagebox.showerror("Error", "Ingresa una cantidad válida")

# Ventana principal
ventana = tk.Tk()
ventana.title("Sistema de Descuentos")
ventana.geometry("300x250")

# Etiquetas y entradas
tk.Label(ventana, text="Total de la compra:").pack(pady=5)
entry_compra = tk.Entry(ventana)
entry_compra.pack()

tk.Label(ventana, text="Color de la bolita:").pack(pady=5)
entry_color = tk.Entry(ventana)
entry_color.pack()

# Botón
tk.Button(ventana, text="Calcular", command=calcular).pack(pady=10)

# Resultado
resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)

ventana.mainloop()