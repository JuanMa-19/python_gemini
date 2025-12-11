import tkinter as tk
import json

# --- MÓDULO C: Lógica de Archivos (Backend) ---

def cargar_datos():
    """Carga el inventario desde json. Se ejecuta UNA SOLA VEZ."""
    try:
        with open('inventario.json', 'r') as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        print("Archivo no encontrado, creando inventario vacío.")
        return []  # <-- ¡CORRECCIÓN! Debe retornar una lista vacía
    except json.JSONDecodeError:
        print("Error en el archivo json, creando inventario vacío.")
        return []

def guardar_datos(inventario_a_guardar):
    """Guarda la lista de inventario en el archivo json."""
    try:
        with open('inventario.json', 'w') as archivo:
            json.dump(inventario_a_guardar, archivo, indent=4)
        print("¡Inventario guardado!")
    except Exception as e:
        print(f"Error al guardar: {e}")

# --- MÓDULO 2 y 3: Lógica de Botones (Frontend) ---

def funcion_anadir():
    """
    Se ejecuta al presionar 'Añadir Producto'.
    Valida y añade el producto a la lista EN MEMORIA.
    """
    # Usamos 'global' para MODIFICAR la lista principal
    global inventario_lista 
    
    try:
        # ¡CORRECCIÓN! Obtenemos de los 'txt_' (Entry), no 'lbl_' (Label)
        nombre = txt_nombre.get()
        precio_str = txt_precio.get()
        stock_str = txt_stock.get()

        # MÓDULO G: Convertir y Validar
        precio = float(precio_str)
        stock = int(stock_str)
        
        if not nombre or precio <= 0 or stock < 0:
            raise ValueError("Datos inválidos")

        # MÓDULO B: Creamos el diccionario
        nuevo_producto = {"nombre": nombre, "precio": precio, "stock": stock}
        inventario_lista.append(nuevo_producto)
        
        # Limpiamos los campos para el siguiente producto
        txt_nombre.delete(0, tk.END)
        txt_precio.delete(0, tk.END)
        txt_stock.delete(0, tk.END)
        
        # Actualizamos la vista para ver el cambio
        funcion_mostrar() 
        
        lbl_mensajes.config(text=f"¡'{nombre}' añadido!", fg="green")
        
    except ValueError:
        lbl_mensajes.config(text="Error: Revisa los datos (Precio/Stock > 0)", fg="red")

def funcion_mostrar():
    """
    Actualiza el cuadro de texto grande con el inventario actual.
    """
    # 1. Borrar el contenido anterior
    cuadro_inventario.delete("1.0", tk.END) # Borra de línea 1, char 0, al final
    
    # 2. Recorrer la lista en memoria y añadir
    if not inventario_lista:
        cuadro_inventario.insert(tk.END, "El inventario está vacío.")
        return
        
    for item in inventario_lista:
        linea = f"Nombre: {item['nombre']} | Precio: S/{item['precio']} | Stock: {item['stock']}\n"
        cuadro_inventario.insert(tk.END, linea)

def al_cerrar():
    """
    Se ejecuta al cerrar la ventana. Guarda los datos.
    """
    print("Guardando inventario al cerrar...")
    guardar_datos(inventario_lista)
    ventana.destroy() # Cierra la ventana

# --- 1. Configuración Inicial ---
inventario_lista = cargar_datos() # Cargamos los datos UNA VEZ

# --- 2. Ventana Principal (Módulo 1) ---
ventana = tk.Tk()
ventana.title("Gestor de Inventario")
ventana.config(padx=20, pady=20)

# --- 3. Widgets del Formulario (Módulo 4: .grid) ---
# (Tu código de formulario estaba perfecto)

# Usamos un Frame para agrupar el formulario
frame_formulario = tk.Frame(ventana, bd=2, relief="groove", padx=10, pady=10)
frame_formulario.grid(row=0, column=0, pady=10)

lbl_nombre = tk.Label(frame_formulario, text="Nombre:")
lbl_nombre.grid(row=0, column=0, sticky="e", padx=5, pady=5)
txt_nombre = tk.Entry(frame_formulario, width=30)
txt_nombre.grid(row=0, column=1, padx=5, pady=5)

lbl_precio = tk.Label(frame_formulario, text="Precio:")
lbl_precio.grid(row=1, column=0, sticky="e", padx=5, pady=5)
txt_precio = tk.Entry(frame_formulario, width=30)
txt_precio.grid(row=1, column=1, padx=5, pady=5)

lbl_stock = tk.Label(frame_formulario, text="Stock:")
lbl_stock.grid(row=2, column=0, sticky="e", padx=5, pady=5)
txt_stock = tk.Entry(frame_formulario, width=30)
txt_stock.grid(row=2, column=1, padx=5, pady=5)

# ¡CORRECCIÓN! Conectamos el 'command' (Módulo 2)
btn_agregar = tk.Button(frame_formulario, text="Añadir Producto", command=funcion_anadir)
btn_agregar.grid(row=3, column=0, columnspan=2, pady=10)

lbl_mensajes = tk.Label(frame_formulario, text="", font=("Arial", 10, "italic"))
lbl_mensajes.grid(row=4, column=0, columnspan=2)

# --- 4. Widgets del Área de Visualización (¡NUEVO!) ---
frame_vista = tk.Frame(ventana)
frame_vista.grid(row=1, column=0, pady=10)

btn_mostrar = tk.Button(frame_vista, text="Actualizar/Mostrar Inventario", command=funcion_mostrar)
btn_mostrar.grid(row=0, column=0, sticky="ew") # sticky="ew" (Este-Oeste)

cuadro_inventario = tk.Text(frame_vista, height=10, width=50)
cuadro_inventario.grid(row=1, column=0, pady=5)

# --- 5. Ejecución ---

# Mostramos los datos que cargamos al inicio
funcion_mostrar() 

# MÓDULO G: Interceptamos el cierre de la ventana
ventana.protocol("WM_DELETE_WINDOW", al_cerrar)

ventana.mainloop()