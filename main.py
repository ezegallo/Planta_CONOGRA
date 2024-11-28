import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Diccionario global para almacenar información de cada celda
celda_info = {}

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Planta CONOGRA S.A.")
ventana.geometry("600x600")
ventana.configure(bg="white")

ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)

texto_inicio = tk.Label(ventana, text="Planta CONOGRA S.A.", font=("Arial", 14), bg="white")
texto_inicio.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")

ruta_logo = "C:/Users/Ezquiel/Desktop/Curso de Python/proyecto_final/imagenes/logo_conogra.png"
imagen = Image.open(ruta_logo)
imagen = imagen.resize((300, 120))
logo = ImageTk.PhotoImage(imagen)

label_logo = tk.Label(ventana, image=logo, bg="white")
label_logo.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

canvas = None
escala = 1.0  # Escala inicial para el zoom

# Función para mostrar el plano de la planta
def ingresar():
    global canvas, escala
    escala = 1.0  # Resetear escala en cada ingreso
    
    # Esconder el contenido inicial
    texto_inicio.grid_forget()
    label_logo.grid_forget()
    boton_ingreso.grid_forget()

    # Crear un Canvas para todo el predio
    canvas = tk.Canvas(ventana, width=800, height=800, bg="white")
    canvas.grid(row=1, column=0, columnspan=2, pady=10)

    dibujar_plano()


def dibujar_plano():
    global canvas
    canvas.delete("all")  # Limpiar el canvas

        # Dibujar la cuadrícula
    filas = 8  # Número de filas
    columnas = 10  # Número de columnas
    width_celda = (500 - 100) / columnas
    height_celda = (300 - 100) / filas

    for i in range(filas):
        for j in range(columnas):
            x1 = 100 + j * width_celda
            y1 = 100 + i * height_celda
            x2 = x1 + width_celda
            y2 = y1 + height_celda
            canvas.create_rectangle(x1, y1, x2, y2, outline="lightgrey", width=1, fill="white", tags=f"celda_{i}_{j}")
            canvas.tag_bind(f"celda_{i}_{j}", "<Button-1>", lambda event, i=i, j=j: cargar_informacion(i, j))

    # Dibujar el contorno del predio (área total)
    canvas.create_rectangle(10 * escala, 50 * escala, 590 * escala, 550 * escala, outline="black", fill="", width=2)

    # Dibujar la planta dentro del predio
    canvas.create_rectangle(100 * escala, 100 * escala, 500 * escala, 300 * escala,
                             outline="black", width=2, fill="", tags="planta")
    canvas.create_text(300 * escala, 80 * escala, text="Planta de Cereal", font=("Arial", int(14 * escala)), fill="black")
    canvas.create_line(300 * escala, 100 * escala, 300 * escala, 300 * escala, fill="green", width=2, dash=(5, 2))

    # Dibujar la zona de maquinaria
    #Clasificadora
    canvas.create_rectangle(180 * escala, 120 * escala, 230 * escala, 170 * escala,
                             outline="red", width=2, fill="lightgray", tags="maquinaria")
    canvas.create_text(205 * escala, 145 * escala, text="Clasifi\ncadora", font=("Arial", int(8 * escala)), fill="black")
    #Vibradora
    canvas.create_rectangle(190 * escala, 180 * escala, 220 * escala, 220 * escala,
                             outline="red", width=2, fill="lightgray", tags="maquinaria")
    canvas.create_text(205 * escala, 200 * escala, text="Vibra\ndora", font=("Arial", int(8 * escala)), fill="black")
    #Oficina
    canvas.create_rectangle(460 * escala, 250 * escala, 500 * escala, 300 * escala,
                             outline="red", width=2, fill="lightgray", tags="maquinaria")
    canvas.create_text(480 * escala, 275 * escala, text="Oficina", font=("Arial", int(8 * escala)), fill="black")
    #Taller
    canvas.create_rectangle(260 * escala, 250 * escala, 300 * escala, 300 * escala,
                             outline="red", width=2, fill="lightgray", tags="maquinaria")
    canvas.create_text(280 * escala, 275 * escala, text="Taller", font=("Arial", int(8 * escala)), fill="black")

    # Dibujar la zona de silos
    canvas.create_oval(100 * escala, 100 * escala, 150 * escala, 150 * escala,
                       outline="blue", width=2, fill="lightblue", tags="Silo Interno")
    canvas.create_text(125 * escala, 125 * escala, text="Silos\nInterno", font=("Arial", int(8 * escala)), fill="black")
    canvas.create_oval(48 * escala, 100 * escala, 98 * escala, 150 * escala,
                       outline="blue", width=2, fill="lightblue", tags="Silo 1")
    canvas.create_text(73 * escala, 125 * escala, text="Silos 1", font=("Arial", int(8 * escala)), fill="black")
    canvas.create_oval(48 * escala, 250 * escala, 98 * escala, 300 * escala,
                       outline="blue", width=2, fill="lightblue", tags="Silo 2")
    canvas.create_text(73 * escala, 275 * escala, text="Silos 2", font=("Arial", int(8 * escala)), fill="black")

# Función para cargar calidad
def calidad():
    calidad_data = {}

    ventana_calidad = tk.Toplevel(ventana)
    ventana_calidad.title("Calidad del Grano")
    ventana_calidad.geometry("300x400")

    def guardar_calidad():
        try:
            calidad_data['Humedad'] = float(entrada_humedad.get())
            calidad_data['Fondo Zaranda'] = float(entrada_fz.get())
            calidad_data['Materia Extraña'] = float(entrada_me.get())
            calidad_data['Grano Dañado'] = float(entrada_dan.get())
            calidad_data['Grano Picado'] = float(entrada_pic.get())
            ventana_calidad.destroy()
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")

    tk.Label(ventana_calidad, text="Humedad (%):").pack(pady=5)
    entrada_humedad = tk.Entry(ventana_calidad)
    entrada_humedad.pack(pady=5)

    tk.Label(ventana_calidad, text="Fondo Zaranda (%):").pack(pady=5)
    entrada_fz = tk.Entry(ventana_calidad)
    entrada_fz.pack(pady=5)

    tk.Label(ventana_calidad, text="Materia Extraña (%):").pack(pady=5)
    entrada_me = tk.Entry(ventana_calidad)
    entrada_me.pack(pady=5)

    tk.Label(ventana_calidad, text="Grano Dañado (%):").pack(pady=5)
    entrada_dan = tk.Entry(ventana_calidad)
    entrada_dan.pack(pady=5)

    tk.Label(ventana_calidad, text="Grano Picado (%):").pack(pady=5)
    entrada_pic = tk.Entry(ventana_calidad)
    entrada_pic.pack(pady=5)

    tk.Button(ventana_calidad, text="Guardar", command=guardar_calidad).pack(pady=20)

    ventana_calidad.wait_window()  # Espera a que la ventana se cierre
    return calidad_data

# Función para cargar la información en la celda
def cargar_informacion(i, j):
    # Verificar si la celda ya tiene información
    if (i, j) in celda_info:
        # Si ya tiene información, no permitir cargar nuevamente, sino solo consultar
        messagebox.showinfo("Información", "Esta celda ya tiene datos cargados. Puedes consultar la información.")
        # Llamar a la función de consulta directamente
        consultar_informacion(i, j)
        return
    ventana_info = tk.Toplevel(ventana)
    ventana_info.title(f"Información de la celda {i},{j}")
    ventana_info.geometry("300x250")

    tipo_grano = tk.StringVar()
    empaque = tk.StringVar()
    cantidad = tk.IntVar()

    def guardar():
        grano = tipo_grano.get()
        tipo_empaque = empaque.get()
        cant = cantidad.get()

        if grano and tipo_empaque and cant:
            respuesta = messagebox.askyesno("Calidad", "¿Deseas ingresar información de calidad?")
            calidad_data = calidad() if respuesta else {}
            guardar_stock((i, j), grano, tipo_empaque, cant, calidad_data)
            ventana_info.destroy()
        else:
            messagebox.showerror("Error", "Todos los campos son obligatorios.")

    tk.Label(ventana_info, text="Tipo de grano:").pack(pady=5)
    tk.Entry(ventana_info, textvariable=tipo_grano).pack(pady=5)

    tk.Label(ventana_info, text="Tipo de Empaque (Bolsas/BigBags):").pack(pady=5)
    tk.Entry(ventana_info, textvariable=empaque).pack(pady=5)

    tk.Label(ventana_info, text="Cantidad Kgs:").pack(pady=5)
    tk.Entry(ventana_info, textvariable=cantidad).pack(pady=5)

    tk.Button(ventana_info, text="Guardar", command=guardar).pack(pady=20)

# Función para colorear celdas según el grano
def colorear_celdas():
    for celda, datos in celda_info.items():
        grano = datos.get('Grano', '').lower()  # Convertir el nombre del grano a minúsculas
        color = ""
        
        # Asignar color según el grano
        if grano == "soja":
            color = "lightyellow"
        elif grano == "mung":
            color = "lightgreen"
        elif grano == "cartamo":
            color = "lightgrey"
        elif grano == "pisingallo":
            color = "lightcoral"
        else:
            color = ''


        # Si hay un color asignado, colorear la celda
        if color:
            i, j = celda
            x1 = 100 + j * ((500 - 100) / 10)  # 10 columnas
            y1 = 100 + i * ((300 - 100) / 8)   # 8 filas
            x2 = x1 + ((500 * escala - 100) / 10)
            y2 = y1 + ((300 * escala - 100) / 8)

            # Dibujar un rectángulo sobre la celda con el color
            canvas.create_rectangle(x1, y1, x2, y2, outline="lightgrey", width=1, fill=color, tags=f"celda_{i}_{j}")

# Función para guardar datos en una celda
def guardar_stock(celda, grano, empaque, cantidad, calidad):
    celda_info[celda] = {
        'Grano': grano,
        'Empaque': empaque,
        'Cantidad': cantidad,
        'Calidad': calidad
    }
    colorear_celdas()  # Llamar a la función para actualizar los colores

def consultar_informacion(i, j):
    # Crear la ventana de consulta de información
    ventana_consulta = tk.Toplevel(ventana)
    ventana_consulta.title(f"Consulta de Celda {i},{j}")
    ventana_consulta.geometry("300x220")

    # Verificar si la celda tiene información almacenada
    if (i, j) in celda_info:
        datos = celda_info[(i, j)]
        grano = datos.get('Grano', 'No especificado')
        empaque = datos.get('Empaque', 'No especificado')
        cantidad = datos.get('Cantidad', 'No especificada')
        calidad = datos.get('Calidad', None)
        
        # Mostrar la información almacenada
        tk.Label(ventana_consulta, text=f"Grano: {grano}").pack(pady=5)
        tk.Label(ventana_consulta, text=f"Empaque: {empaque}").pack(pady=5)
        tk.Label(ventana_consulta, text=f"Cantidad: {cantidad} Kgs").pack(pady=5)
        
        def mover_estiba():
            # Crear ventana para mover la estiba
            ventana_mover = tk.Toplevel(ventana_consulta)
            ventana_mover.title(f"Seleccionar nueva celda para {grano}")
            ventana_mover.geometry("300x200")

            tk.Label(ventana_mover, text="Celda destino:").pack(pady=5)

            # Cuadro de texto para mostrar la celda seleccionada
            cuadro_celda_destino = tk.Entry(ventana_mover, justify="center", font=("Arial", 12))
            cuadro_celda_destino.pack(pady=10)

            # Instrucción para el usuario
            tk.Label(ventana_mover, text="Haz clic derecho sobre una celda en el plano para seleccionarla.").pack(pady=5)

            # Función para mover los datos a la celda destino
            def confirmar_movimiento():
                destino = cuadro_celda_destino.get()  # Obtener la celda destino ingresada
                try:
                    destino_i, destino_j = map(int, destino.split(","))
                    if destino_i < 0 or destino_i >= 8 or destino_j < 0 or destino_j >= 10:
                        tk.Label(ventana_mover, text="Seleccione una celda dentro de la Planta").pack(pady=5)
                    elif (destino_i, destino_j) not in celda_info:
                        # Mover la información
                        celda_info[(destino_i, destino_j)] = celda_info.pop((i, j))
                        tk.Label(ventana_mover, text=f"Mercadería movida a la celda {destino}.").pack(pady=10)
                        ventana_mover.after(2000, ventana_mover.destroy)
                        ventana_consulta.destroy()
                    else:
                        tk.Label(ventana_mover, text="La celda de destino ya está ocupada.").pack(pady=5)
                except ValueError:
                    tk.Label(ventana_mover, text="Formato inválido. Usa el formato 'fila,columna'.").pack(pady=5)
                dibujar_plano()
                colorear_celdas()

            # Botón para confirmar el movimiento
            tk.Button(ventana_mover, text="Confirmar Movimiento", command=confirmar_movimiento).pack(pady=10)

        # Botón para mover la estiba
        tk.Button(ventana_consulta, text="Mover Estiba", command=mover_estiba).pack(pady=10)

        # Botón para consultar análisis de calidad
        if calidad:
            # Si tiene calidad, mostrar los detalles
            ventana_consulta.geometry("300x350")
            tk.Label(ventana_consulta, text="Análisis de Calidad:").pack(pady=5)
            for parametro, valor in calidad.items():
                tk.Label(ventana_consulta, text=f"{parametro}: {valor}%").pack(pady=3)
            tk.Button(ventana_consulta, text="Cerrar", command=ventana_consulta.destroy).pack(pady=10)
        else:
            # Si no tiene calidad, permitir agregarla
            tk.Button(ventana_consulta, text="Agregar Análisis de Calidad", 
                      command=lambda: agregar_calidad(i, j)).pack(pady=10)
            
    else:
        # Si no tiene información almacenada, mostrar un mensaje
        tk.Label(ventana_consulta, text="Esta celda no tiene información almacenada.").pack(pady=10)
        tk.Button(ventana_consulta, text="Cerrar", command=ventana_consulta.destroy).pack(pady=20)

# Función para agregar análisis de calidad
def agregar_calidad(i, j):
    calidad_data = calidad()
    if calidad_data:
        celda_info[(i, j)]['Calidad'] = calidad_data
        messagebox.showinfo("Información", "Análisis de calidad agregado correctamente.")


# Crear el botón de ingreso
boton_ingreso = tk.Button(ventana, text="Ingresar al Sistema", font=("Arial", 12), command=ingresar)
boton_ingreso.grid(row=2, column=0, columnspan=2, pady=20)

ventana.mainloop()
