import tkinter as tk
from PIL import Image, ImageTk

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Planta CONOGRA S.A.")
ventana.geometry("600x600")
ventana.configure(bg="white")

# Configurar las filas y columnas para que se distribuyan de manera uniforme
ventana.grid_columnconfigure(0, weight=1)
ventana.grid_columnconfigure(1, weight=1)
ventana.grid_rowconfigure(0, weight=1)
ventana.grid_rowconfigure(1, weight=1)

# Agregar un texto usando grid
texto_inicio = tk.Label(ventana, text="Planta CONOGRA S.A.", font=("Arial", 14), bg="white")
texto_inicio.grid(row=0, column=0, columnspan=2, pady=20, sticky="nsew")

# Cargar la imagen PNG (sin transparencia)
ruta_logo = "C:/Users/Ezquiel/Desktop/Curso de Python/proyecto_final/imagenes/logo_conogra.png"
imagen = Image.open(ruta_logo)
imagen = imagen.resize((300, 120))
logo = ImageTk.PhotoImage(imagen)

# Mostrar el logo en la ventana
label_logo = tk.Label(ventana, image=logo, bg="white")
label_logo.grid(row=1, column=0, columnspan=2, pady=10, sticky="nsew")

# Crear el canvas global para zoom
canvas = None
escala = 1.0  # Escala inicial para el zoom


# Función para mostrar el plano de la planta
def ingresar():
    global canvas, escala
    escala = 1.0  # Resetear escala en cada ingreso
    
    # Esconder el contenido inicial (texto y logo)
    texto_inicio.grid_forget()
    label_logo.grid_forget()
    boton_ingreso.grid_forget()

    # Crear un Canvas para todo el predio
    canvas = tk.Canvas(ventana, width=800, height=800, bg="white")
    canvas.grid(row=1, column=0, columnspan=2, pady=10)

    # Dibujar el plano inicial
    dibujar_plano()

    # Asignar la función de clic al canvas
    canvas.bind("<Button-1>", clic_zona)
    # Asignar el zoom al evento de la rueda del mouse
    canvas.bind("<MouseWheel>", zoom)


# Dibujar los elementos del plano
def dibujar_plano():
    global canvas, escala
    canvas.delete("all")  # Limpiar el canvas

    # Dibujar el contorno del predio (área total)
    canvas.create_rectangle(10 * escala, 50 * escala, 590 * escala, 550 * escala, outline="black", width=2)

    # Dibujar la planta dentro del predio
    canvas.create_rectangle(100 * escala, 100 * escala, 500 * escala, 300 * escala,
                             outline="black", width=2, fill="white", tags="planta")
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


# Función para manejar los clics en las zonas
def clic_zona(event):
    x, y = event.x, event.y
    print(f"Clic en las coordenadas: {x}, {y}")


# Función para manejar el zoom
def zoom(event):
    global escala
    if event.delta > 0:  # Rueda hacia arriba -> Zoom IN
        escala *= 1.1
    elif event.delta < 0:  # Rueda hacia abajo -> Zoom OUT
        escala /= 1.1
    dibujar_plano()  # Redibujar el plano con la nueva escala


# Crear el botón de ingreso
boton_ingreso = tk.Button(ventana, text="Ingreso al Sistema", command=ingresar, font=("Arial", 12))
boton_ingreso.grid(row=2, column=0, columnspan=2, pady=20, sticky="nsew")

# Ejecutar la ventana principal
ventana.mainloop()
