import tkinter as tk

def escribir_diario():
    titulo = entry_titulo.get()
    clave = entry_clave.get()
    texto = text_mensaje.get("1.0", "end-1c")
    print(f"Titulo: {titulo} | Clave: {clave}\nTexto: {texto}")

ventana = tk.Tk()
ventana.title("Mi diario")
ventana.geometry("300x300")
ventana.config(padx=20, pady=20)
#---------------
tk.Label(ventana, text="Titulo: ").grid(row=0, column=0, padx=5, pady=5, sticky="e")
entry_titulo = tk.Entry(ventana, width=30)
entry_titulo.grid(row=0, column=1, padx=5, pady=5)
#---------------
tk.Label(ventana, text="Clave:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
entry_clave = tk.Entry(ventana, width=30, show="*")
entry_clave.grid(row=1, column=1, padx=5, pady=5)
#---------------
tk.Label(ventana, text="Mensaje: ").grid(row=2, column=0, padx=5, pady=5, sticky="e")
text_mensaje = tk.Text(ventana, width=22, height=5)
text_mensaje.grid(row=2, column=1, padx=5, pady=5)
#---------------
tk.Button(ventana, text="Guardar Nota", command=escribir_diario).grid(row=3, column=0, columnspan=2, padx=5, pady=5)
ventana.mainloop()