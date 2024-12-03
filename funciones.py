def consultar_informacion(i, j):
    # Crear la ventana de consulta de información
    ventana_consulta = tk.Toplevel(ventana)
    ventana_consulta.title(f"Consulta de Celda {i},{j}")
    ventana_consulta.geometry("300x330")

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

        # Botón para consultar análisis de calidad
        if calidad:
            # Si tiene calidad, mostrar los detalles
            tk.Label(ventana_consulta, text="Análisis de Calidad:").pack(pady=5)
            for parametro, valor in calidad.items():
                tk.Label(ventana_consulta, text=f"{parametro}: {valor}%").pack(pady=3)
            tk.Button(ventana_consulta, text="Cerrar", command=ventana_consulta.destroy).pack(pady=20)
        else:
            # Si no tiene calidad, permitir agregarla
            tk.Button(ventana_consulta, text="Consultar Análisis de Calidad", 
                      command=lambda: agregar_calidad(i, j)).pack(pady=10)
            tk.Button(ventana_consulta, text="Agregar Análisis de Calidad", 
                      command=lambda: agregar_calidad(i, j)).pack(pady=10)

        # Botón para mover la estiba
        tk.Button(ventana_consulta, text="Mover Estiba", 
                  command=lambda: mover_estiba(i, j, ventana_consulta)).pack(pady=10)
        
        # Botón para cargar la estiba
        tk.Button(ventana_consulta, text="Cargar Estiba", 
                  command=lambda: cargar_estiba(i, j, ventana_consulta)).pack(pady=10)

    else:
        # Si no tiene información almacenada, mostrar un mensaje
        tk.Label(ventana_consulta, text="Esta celda no tiene información almacenada.").pack(pady=10)
        tk.Button(ventana_consulta, text="Cerrar", command=ventana_consulta.destroy).pack(pady=20)


# Función para mover la estiba (grano) de una celda a otra
def mover_estiba(i, j, ventana):
    # Crear una ventana para seleccionar la celda de destino
    ventana_mover = tk.Toplevel(ventana)
    ventana_mover.title("Seleccionar Celda de Destino")
    ventana_mover.geometry("300x300")

    # Mostrar las celdas disponibles para mover el grano
    tk.Label(ventana_mover, text="Selecciona la celda de destino").pack(pady=10)

    # Aquí generaríamos una grilla de celdas para que el usuario seleccione el destino
    # O puede ser un cuadro de texto o botones para seleccionar las celdas
    for x in range(5):  # Ejemplo con 5 celdas disponibles
        for y in range(5):  # 5 filas y columnas
            boton = tk.Button(ventana_mover, text=f"({x},{y})", 
                              command=lambda x=x, y=y: confirmar_movimiento(i, j, x, y, ventana_mover))
            boton.grid(row=x, column=y, padx=5, pady=5)

# Función para confirmar el movimiento de la estiba
def confirmar_movimiento(i, j, x_destino, y_destino, ventana_mover):
    # Verificar si la celda de destino está vacía
    if (x_destino, y_destino) not in celda_info:
        # Mover la estiba (copiar la información de la celda origen a destino)
        celda_info[(x_destino, y_destino)] = celda_info.pop((i, j))
        # Cerrar la ventana de movimiento
        ventana_mover.destroy()
        print(f"Estiba movida de ({i}, {j}) a ({x_destino}, {y_destino})")
    else:
        tk.messagebox.showwarning("Error", "La celda de destino ya está ocupada.")

# Función para cargar la estiba (liberar la celda)
def cargar_estiba(i, j, ventana):
    # Eliminar la información de la celda, marcando como vacía
    if (i, j) in celda_info:
        del celda_info[(i, j)]
        tk.messagebox.showinfo("Carga Completada", f"Celda ({i}, {j}) liberada por carga.")
    else:
        tk.messagebox.showwarning("Error", "La celda ya está vacía.")
    
    # Cerrar la ventana de consulta
    ventana.destroy()
