import tkinter as tk

def obtener_datos():
    usuario = entry_usuario.get()
    clave = entry_clave.get()
    
    # "1.0" significa: Desde la línea 1, carácter 0
    # "end-1c" significa: Hasta el final, menos el último salto de línea
    bio = text_bio.get("1.0", "end-1c")
    
    print(f"Usuario: {usuario} | Clave: {clave}")
    print(f"Biografia: {bio}")

ventana = tk.Tk()
ventana.title("Nivel 1: Textos")
ventana.geometry("300x250")
ventana.config(padx=20, pady=20) # Margen interno para toda la ventana
#-----------------------f0
tk.Label(ventana, text="Usuario:").grid(row=0, column=0, sticky="e", pady=5, padx=5)
entry_usuario = tk.Entry(ventana, width=30)
entry_usuario.grid(row=0, column=1, padx=5, pady=5)
#-----------------------f1
tk.Label(ventana, text="Contraseña:").grid(row=1, column=0, sticky="e", pady=5, padx=5)
entry_clave = tk.Entry(ventana, width=30, show="*")
entry_clave.grid(row=1, column=1, padx=5, pady=5)
#-----------------------f2
tk.Label(ventana, text="Biografia:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
text_bio = tk.Text(ventana, width=22, height=5)
text_bio.grid(row=2, column=1, padx=5, pady=5)
#-----------------------f3
tk.Button(ventana, text="Guardar datos", command=obtener_datos).grid(row=3, column=0, columnspan=2, pady=20)
ventana.mainloop()