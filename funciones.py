
# celda_info = {}
# celda = 1

# def guardar_stock(celda, grano, empaque, cantidad, calidad):
#     global celda_info
#     grano = input('Ingrese Grano Almacenado: ')
#     empaque = input('Ingrese si el grano esta en Bolsas o Big Bag: ')
#     cantidad = int(input('Ingrese la cantidad almacenada en Kgs: '))
#     calidad = calidad()
#     celda_info[celda] = {'Grano': grano, 'Empaque':empaque, 'Cantidad': cantidad, 'Calidad': calidad}

# def calidad(humedad, fondo_zaranda, materia_extraña, grano_dañado, grano_picado):
#     humedad = float(input('Ingrese % Humedad del Grano: '))
#     fondo_zaranda = float(input('Ingrese % F/Z: '))
#     materia_extraña = float(input('Ingrese % ME del Grano: '))
#     grano_dañado = float(input('Ingrese % de Grano Dañado: '))
#     grano_picado = float(input('Ingrese % de Grano Picado: '))


# guardar_stock()

celda_info = {}  # Diccionario global para almacenar la información de cada celda

# Función para guardar información en una celda específica
def guardar_stock(celda):
    global celda_info  # Usamos el diccionario global
    grano = input('Ingrese Grano Almacenado: ')
    empaque = input('Ingrese si el grano está en Bolsas o Big Bag: ')
    cantidad = int(input('Ingrese la cantidad almacenada en Kgs: '))
    # Llamamos a la función calidad para obtener un diccionario con los datos de calidad
    calidad_info = calidad()
    # Guardamos toda la información en el diccionario global
    celda_info[f'Celda{celda}'] = {'Grano': grano, 'Empaque': empaque, 'Cantidad': cantidad, 'Calidad': calidad_info}

# Función para recopilar datos de calidad
def calidad():
    humedad = float(input('Ingrese % de Humedad del Grano: '))
    fondo_zaranda = float(input('Ingrese % de Fondo/Zaranda: '))
    materia_extraña = float(input('Ingrese % de Materia Extraña del Grano: '))
    grano_dañado = float(input('Ingrese % de Grano Dañado: '))
    grano_picado = float(input('Ingrese % de Grano Picado: '))
    # Retornamos un diccionario con los datos
    return {
        'Humedad': humedad,
        'Fondo/Zaranda': fondo_zaranda,
        'Materia Extraña': materia_extraña,
        'Grano Dañado': grano_dañado,
        'Grano Picado': grano_picado
    }

# Llamar a la función guardar_stock para la celda 1
guardar_stock(1)

# Mostrar la información guardada
print("\nInformación almacenada:")
print(celda_info)