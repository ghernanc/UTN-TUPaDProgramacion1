
# tp7_ejercicio8.py
# Objetivo: Armar un diccionario de stock (producto -> unidades) y permitir:
#   - Consultar stock de un producto ingresado
#   - Agregar unidades si el producto existe
#   - Agregar un producto nuevo si no existe

# Creamos el diccionario de stock vacío.
stock = {}

# Mostramos un menú simple para interactuar con el stock.
while True:
    # Presentamos opciones al usuario.
    print('\n--- Gestión de Stock ---')
    print('1) Consultar stock de un producto')
    print('2) Agregar unidades a un producto existente')
    print('3) Agregar un producto nuevo')
    print('4) Ver todo el stock')
    print('5) Salir')

    # Leemos la opción elegida.
    opcion = input('Elegí una opción (1-5): ').strip()

    # Opción 1: consultar stock de un producto
    if opcion == '1':
        producto = input('Ingresá el nombre del producto: ').strip()
        if producto in stock:
            print(f'Stock de "{producto}": {stock[producto]} unidades')
        else:
            print(f'El producto "{producto}" no existe en el stock.')

    # Opción 2: agregar unidades
    elif opcion == '2':
        producto = input('Producto a actualizar: ').strip()
        if producto in stock:
            try:
                unidades = int(input('¿Cuántas unidades querés agregar?: ').strip())
                stock[producto] += max(0, unidades)  # Evitamos restar por accidente
                print(f'Nuevo stock de "{producto}": {stock[producto]} unidades')
            except ValueError:
                print('Por favor ingresá un número entero válido.')
        else:
            print(f'El producto "{producto}" no existe. Usá la opción 3 para crearlo.')

    # Opción 3: agregar un producto nuevo
    elif opcion == '3':
        producto = input('Nombre del nuevo producto: ').strip()
        if producto in stock:
            print(f'El producto "{producto}" ya existe con {stock[producto]} unidades.')
        else:
            try:
                unidades = int(input('Unidades iniciales: ').strip())
                stock[producto] = max(0, unidades)  # No permitir negativos
                print(f'Se agregó "{producto}" con {stock[producto]} unidades.')
            except ValueError:
                print('Por favor ingresá un número entero válido.')

    # Opción 4: ver todo el stock
    elif opcion == '4':
        if stock:
            print('Stock completo:')
            for prod, unidades in stock.items():
                print(f' - {prod}: {unidades}')
        else:
            print('Aún no hay productos cargados.')

    # Opción 5: salir del programa
    elif opcion == '5':
        print('Saliendo del gestor de stock. ¡Hasta luego!')
        break

    # Cualquier otra opción no es válida
    else:
        print('Opción inválida. Elegí entre 1 y 5.')
