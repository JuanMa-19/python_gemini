import tkinter as tk

def calcular_area():
    try:
        base = float(ent_base.get())
        altura = float(ent_altura.get())
        
        area = base * altura
        lbl_area.config(text=f"El área del rectangulo es: {area}")
    except ValueError:
        lbl_area.config(text="Hábil te crees")

ventana = tk.Tk()
ventana.title("Calculadora de Área")
ventana.geometry("400x300")

lbl_mensaje = tk.Label(ventana, text="Calculadora de Área Rectangular")
lbl_mensaje.pack(pady=5)

lbl_base = tk.Label(ventana, text="Ingresa la base: ")
lbl_base.pack(pady=5)

ent_base = tk.Entry(ventana)
ent_base.pack(pady=5)

lbl_altura = tk.Label(ventana, text="Ingresa la altura: ")
lbl_altura.pack(pady=5)

ent_altura = tk.Entry(ventana)
ent_altura.pack(pady=5)

btn_calcular_area = tk.Button(ventana, text="Calcular",command=calcular_area)
btn_calcular_area.pack(pady=10)

lbl_area = tk.Label(ventana, text="")
lbl_area.pack(pady=5)

ventana.mainloop()