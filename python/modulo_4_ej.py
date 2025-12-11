import tkinter as tk

def calcular_area():
    try:
        base = float(txt_base.get())
        altura = float(txt_altura.get())

        lbl_resultado.config(text=f"El área es: {base*altura}")
        
    except ValueError:
        lbl_resultado.config(text="Tienes que ingresar numeros ctm")

ventana = tk.Tk()
ventana.title("Calculadora de Área 2.0")
ventana.config(padx=20, pady=20)

lbl_base = tk.Label(ventana, text="Ingresa la base:")
lbl_base.grid(row=0, column=0, sticky="e")

txt_base = tk.Entry(ventana)
txt_base.grid(row=0, column=1)

lbl_altura = tk.Label(ventana, text="Ingresa la altura: ")
lbl_altura.grid(row=1, column=0, sticky="e")

txt_altura = tk.Entry(ventana)
txt_altura.grid(row=1, column=1)

btn_calcular = tk.Button(ventana, text="Calcular", command=calcular_area)
btn_calcular.grid(row=2, column=0, columnspan=2, pady=20)

lbl_resultado = tk.Label(ventana, text="")
lbl_resultado.grid(row=3, column=0, columnspan=2)

ventana.mainloop()