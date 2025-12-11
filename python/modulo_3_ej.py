import tkinter as tk

def convertir():
    celsius = float(entry_celsius.get()) 
    conv_faren = (celsius * 9/5) + 32
    label_conversion.config(text=f"Los grados Fahrenheit es: {conv_faren}")
    
""" 
def convertir():
    try:
        celsius_str = entry_celsius.get()
        celsius = float(celsius_str) 
        conv_faren = (celsius * 9/5) + 32
        label_conversion.config(text=f"Los grados Fahrenheit es: {conv_faren}°F")
    except ValueError:
        # Esto se ejecuta si 'float(celsius_str)' falla
        label_conversion.config(text="Error: Introduce solo números")
"""

ventana = tk.Tk()
ventana.title("Conversion de grados")
ventana.geometry("400x200")

label_mensaje = tk.Label(ventana, text="Ingresa los grados Celsius")
label_mensaje.pack(pady=5)

entry_celsius = tk.Entry(ventana)
entry_celsius.pack(pady=5)

button_convertir = tk.Button(ventana, text="Convertir", command=convertir)
button_convertir.pack(pady=10)

label_conversion = tk.Label(ventana, text="")
label_conversion.pack(pady=5)

ventana.mainloop()