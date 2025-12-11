import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi Perfil")
ventana.geometry("400x200")

etiqueta = tk.Label(ventana, text="Hola soy Juan Manuel Quispe Carbajal")
etiqueta.pack(pady=30)

ventana.mainloop()