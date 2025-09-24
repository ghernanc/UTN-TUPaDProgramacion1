#10) Una tienda registra las ventas de 4 productos durante 7 días, en una matriz de 4x7.
#• Mostrar el total vendido por cada producto.
#• Mostrar el día con mayores ventas totales.
#• Indicar cuál fue el producto más vendido en la semana.
# Matriz de ventas: 4 productos x 7 días (cada fila = producto, cada columna = día)
ventas = [                                  # Matriz de ventas: 4 productos (filas) x 7 días (columnas)
    [10, 8, 2, 9, 10, 6, 7],                # Ventas del producto 1 en los 7 días
    [6, 1, 9, 10, 8, 2, 5],                 # Ventas del producto 2 en los 7 días
    [9, 10, 6, 9, 10, 6, 4],                # Ventas del producto 3 en los 7 días
    [7, 4, 10, 6, 9, 10, 3],                # Ventas del producto 4 en los 7 días
]

totales_productos = []                      # Lista donde guardaremos el total semanal de cada producto

# Total vendido por cada producto (suma por filas)
for i in range(len(ventas)):                # i recorre los productos (índices de filas: 0..3)
    total_producto = 0                      # Acumulador del total del producto i
    for j in range(len(ventas[0])):         # j recorre los días (índices de columnas: 0..6)
        total_producto += ventas[i][j]      # Sumo la venta del producto i en el día j
    totales_productos.append(total_producto)# Guardo el total del producto i en la lista
    print(f"El total del producto {i+1}: {total_producto}")  # Muestro el total del producto (i+1 para humano)

# Día con mayores ventas (suma por columnas)
mayor_ventas = 0                            # Máximo de ventas totales encontrado para un día
dia_mayor = 0                               # Índice del día con mayor venta total (0..6)

for j in range(len(ventas[0])):             # j recorre los días (columnas)
    total_dia = 0                           # Acumulador de ventas del día j
    for i in range(len(ventas)):            # i recorre los productos (filas)
        total_dia += ventas[i][j]           # Sumo la venta del producto i en el día j
    print(f"El total del día {j+1}: {total_dia}")            # Muestro el total del día (j+1 para humano)
    if total_dia > mayor_ventas:            # Si este día supera el máximo anterior
        mayor_ventas = total_dia            # Actualizo el máximo
        dia_mayor = j                       # Guardo el índice del día con máximo

print(f"\nEl día con mayores ventas fue el {dia_mayor+1}, con {mayor_ventas} ventas")  # Resultado del día top

# Producto más vendido en la semana (máximo entre totales por producto)
mayor_producto = 0                          # Mayor total semanal encontrado entre productos
indice_mayor = 0                            # Índice del producto con mayor total

for i in range(len(totales_productos)):     # Recorro los totales de cada producto
    if totales_productos[i] > mayor_producto:  # Si el total del producto i es mayor al máximo actual
        mayor_producto = totales_productos[i]  # Actualizo el máximo
        indice_mayor = i                        # Guardo qué producto es

print(f"\nEl producto más vendido fue el {indice_mayor+1}, con {mayor_producto} ventas en la semana")  # Resultado final
