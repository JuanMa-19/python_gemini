import tkinter as tk

def saludar_usuario():
    nombre = campo_nombre.get()
    etiqueta_saludo.config(text=f"Hola, {nombre}!!")

ventana = tk.Tk()
ventana.title("App de Saludos")
ventana.geometry("350x200")

etiqueta_instruccion = tk.Label(ventana, text="Escribe tu nombre")
etiqueta_instruccion.pack(pady=5)

campo_nombre = tk.Entry(ventana)
campo_nombre.pack(pady=5)

boton_saludar = tk.Button(ventana, text="Saludar", command=saludar_usuario)
boton_saludar.pack(pady=10)

etiqueta_saludo = tk.Label(ventana, text="")
etiqueta_saludo.pack(pady=20)

ventana.mainloop()