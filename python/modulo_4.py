import tkinter as tk

ventana = tk.Tk()
ventana.title("Usando .grid()")
#.config() en la ventana para añadir espacio interior
ventana.config(padx=20, pady=20)

#fila 0 
lbl_usuario = tk.Label(ventana, text="Usuario:")
#colocamos en la fila 0, colm 0, sticky = "w", lo alinea a la izq
lbl_usuario.grid(row=0, column=0, sticky="w")

"""
N:arriba
E:derecha
S:abajo
W:izquierda
"""

txt_usuario = tk.Entry(ventana)
txt_usuario.grid(row=0, column=1, pady=5, padx=5)

#fila 1
lbl_pass = tk.Label(ventana, text="Contraseña:")
lbl_pass.grid(row=1, column=0, sticky="w")

txt_pass = tk.Entry(ventana, show="*")
txt_pass.grid(row=1, column=1, pady=5, padx=5)

#fila 2
btn_login = tk.Button(ventana, text="Iniciar Sesión")
#hacemos que use 2 columnas y se centre (por defecto)
btn_login.grid(row=2, column=0, columnspan=2, pady=10)


ventana.mainloop()