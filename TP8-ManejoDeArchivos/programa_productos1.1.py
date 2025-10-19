# ---------------------------------------------------------
# 1. Leer productos desde el archivo (no lo crea)
# ---------------------------------------------------------
def leer_productos(nombre_archivo):
    productos = []  # Lista vacía donde se guardarán los productos leídos

    try:
        # Intenta abrir el archivo en modo lectura ("r")
        with open(nombre_archivo, "r") as archivo:
            # Recorre cada línea del archivo
            for linea in archivo:
                linea = linea.strip()  # Quita espacios o saltos de línea
                if not linea:          # Si la línea está vacía, la salta
                    continue
                partes = linea.split(",")  # Divide la línea en 3 partes separadas por coma
                if len(partes) == 3:       # Verifica que haya exactamente 3 datos
                    nombre, precio, cantidad = partes  # Asigna cada parte a una variable
                    productos.append({                 # Agrega un diccionario a la lista
                        "nombre": nombre,
                        "precio": float(precio),       # Convierte el precio a número decimal
                        "cantidad": int(cantidad)      # Convierte la cantidad a número entero
                    })
    except FileNotFoundError:
        # Si el archivo no existe, muestra un mensaje de aviso
        print(f"No se encontró el archivo '{nombre_archivo}'. Crealo a mano antes de usar el programa.")

    return productos  # Devuelve la lista de productos leídos


# ---------------------------------------------------------
# 2. Guardar productos (sobrescribe el archivo)
# ---------------------------------------------------------
def guardar_productos(nombre_archivo, productos):
    # Abre el archivo en modo escritura ("w") → sobrescribe todo el contenido
    with open(nombre_archivo, "w") as archivo:
        # Recorre cada producto en la lista
        for p in productos:
            # Escribe una línea con los tres datos separados por coma
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")


# ---------------------------------------------------------
# 3. Mostrar productos
# ---------------------------------------------------------
def mostrar_productos(productos):
    print("\n--- LISTA DE PRODUCTOS ---")  # Título
    if not productos:                      # Si la lista está vacía
        print("(Vacío o archivo no encontrado)")
        return
    # Muestra cada producto con su nombre, precio y cantidad
    for p in productos:
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")


# ---------------------------------------------------------
# 4. Agregar producto (lee lista, agrega y guarda)
# ---------------------------------------------------------
def agregar_producto(nombre_archivo):
    productos = leer_productos(nombre_archivo)  # Lee los productos actuales del archivo

    # Pide al usuario los datos del nuevo producto
    nombre = input("Nombre del producto: ").strip()
    precio = float(input("Precio: ").replace(",", "."))  # Reemplaza coma por punto si el usuario la usa
    cantidad = int(input("Cantidad: "))

    # Crea un diccionario con el nuevo producto y lo agrega a la lista
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})

    # Guarda toda la lista nuevamente (sobrescribiendo el archivo)
    guardar_productos(nombre_archivo, productos)
    print("Producto agregado y archivo actualizado correctamente.")


# ---------------------------------------------------------
# 5. Buscar producto por nombre
# ---------------------------------------------------------
def buscar_producto(productos):
    if not productos:  # Si no hay productos cargados
        print("No hay productos cargados o el archivo no existe.")
        return

    # Pide el nombre del producto a buscar
    nombre = input("Ingrese el nombre del producto a buscar: ").strip()

    # Recorre la lista de productos buscando coincidencias
    for p in productos:
        if p["nombre"].lower() == nombre.lower():  # Compara sin importar mayúsculas/minúsculas
            # Si lo encuentra, muestra sus datos
            print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
            return
    # Si no lo encuentra, muestra un mensaje
    print("El producto no existe en la lista.")


# ---------------------------------------------------------
# 6. Eliminar producto(s) por nombre
# ---------------------------------------------------------
def eliminar_productos(nombre_archivo):
    productos = leer_productos(nombre_archivo)  # Carga todos los productos
    if not productos:  # Si la lista está vacía, avisa
        print("No hay productos cargados o el archivo no existe.")
        return

    # Pide al usuario el nombre del producto a eliminar
    nombre = input("Ingrese el nombre del producto a eliminar: ").strip().lower()

    # Crea una nueva lista con los productos que no coincidan con el nombre
    restantes = [p for p in productos if p["nombre"].lower() != nombre]

    # Calcula cuántos productos se eliminaron
    eliminados = len(productos) - len(restantes)

    if eliminados == 0:
        print("El producto no existe en la lista.")
        return

    # Guarda la lista actualizada en el archivo
    guardar_productos(nombre_archivo, restantes)
    print(f"Se eliminaron {eliminados} producto(s) con el nombre indicado.")


# ---------------------------------------------------------
# 7. Menú principal
# ---------------------------------------------------------
def main():
    archivo = "productos.txt"  # Nombre del archivo con los datos

    while True:  # Bucle que mantiene el menú activo
        # Muestra las opciones del menú
        print("\n===== MENÚ PRINCIPAL =====")
        print("1. Agregar producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar producto por nombre")
        print("4. Eliminar producto(s) por nombre")
        print("5. Salir")

        # Pide la opción al usuario
        opcion = input("Seleccione una opción (1-5): ").strip()

        # Según la opción elegida, ejecuta la función correspondiente
        if opcion == "1":
            agregar_producto(archivo)

        elif opcion == "2":
            productos = leer_productos(archivo)
            mostrar_productos(productos)

        elif opcion == "3":
            productos = leer_productos(archivo)
            buscar_producto(productos)

        elif opcion == "4":
            eliminar_productos(archivo)

        elif opcion == "5":
            print("Hasta luego")  # Sale del programa
            break

        else:
            # Si el usuario ingresa algo distinto a 1–5
            print("Opción inválida. Intente nuevamente.")
# ---------------------------------------------------------
# 8. Punto de entrada del programa
# ---------------------------------------------------------
if __name__ == "__main__":
    main()  # Llama a la función principal cuando se ejecuta el archivo

