import tkinter as tk

# crear la ventana principal
ventana = tk.Tk()
ventana.title("Mi Aplicación Tkinter")
ventana.geometry("300x150")

#crea un widget
# le decimos que su padre es la ventana
etiqueta = tk.Label(ventana, text="Hola mundo de tkinter")

#3 colocamos el widget en la ventana
etiqueta.pack(pady=20) #pady añade espacio vertical

#4 iniciar el bucle de eventos
ventana.mainloop()
