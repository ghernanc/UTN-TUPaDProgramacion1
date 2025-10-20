# ==========================
# GESTIÓN DE PRODUCTOS 
# ==========================

# ---------- Funciones de validación ----------

def es_entero_no_negativo(txt: str) -> bool:  # Verifica si el texto contiene solo dígitos
    return txt.isdigit()  # Devuelve True si todos los caracteres son números

def es_float_no_negativo_simple(txt: str) -> bool:  # Verifica si un texto es un número decimal válido
    if not txt:  # Si está vacío, retorna False
        return False
    t = txt.strip().replace(",", ".")  # Reemplaza coma por punto
    if t.count(".") > 1:  # Si hay más de un punto, no es válido
        return False
    if t == ".":  # Si es solo un punto, tampoco es válido
        return False
    if "." in t:  # Si tiene punto decimal
        a, b = t.split(".")  # Divide parte entera y decimal
        if a == "" and b == "":  # Si ambas están vacías
            return False
        if (a != "" and not a.isdigit()) or (b != "" and not b.isdigit()):
            return False
        return True
    return t.isdigit()  # Si no tiene punto, debe ser entero

def pedir_entero_no_negativo(mensaje: str) -> int:  # Pide un número entero no negativo al usuario
    valor = input(mensaje).strip()  # Solicita entrada y quita espacios
    while not es_entero_no_negativo(valor):  # Repite mientras no sea número válido
        print("Ingrese un número entero válido (>= 0).")
        valor = input(mensaje).strip()
    return int(valor)  # Devuelve el valor convertido a entero

def pedir_float_no_negativo(mensaje: str) -> float:  # Pide un número decimal al usuario
    valor = input(mensaje).strip()  # Solicita y limpia
    while not es_float_no_negativo_simple(valor):  # Repite mientras no sea válido
        print("Ingrese un número válido (>= 0). Use punto o coma para decimales.")
        valor = input(mensaje).strip()
    return float(valor.replace(",", "."))  # Devuelve el número como float

def pedir_texto_no_vacio(mensaje: str) -> str:  # Pide texto que no esté vacío
    txt = input(mensaje).strip()  # Solicita y limpia espacios
    while " ".join(txt.split()) == "":  # Repite si está vacío o solo tiene espacios
        print("El texto no puede estar vacío.")
        txt = input(mensaje).strip()
    return txt  # Devuelve el texto válido


# ---------- Leer productos del archivo ----------

def leer_productos(nombre_archivo):
    productos = []  # Lista donde se guardarán los productos

    with open(nombre_archivo, "a+", encoding="utf-8") as archivo:  # Abre el archivo (lo crea si no existe)
        archivo.seek(0)  # Mueve el cursor al inicio para leer
        for linea in archivo:  # Recorre línea por línea
            linea = linea.strip()  # Elimina saltos de línea
            if not linea:  # Si está vacía, la ignora
                continue
            partes = linea.split(",")  # Divide la línea en nombre, precio y cantidad
            if len(partes) != 3:  # Si no tiene 3 partes, se salta
                continue

            nombre, precio_txt, cantidad_txt = partes  # Asigna cada parte
            nombre = nombre.strip()  # Limpia el nombre
            precio_txt = precio_txt.strip().replace(",", ".")  # Reemplaza coma por punto
            cantidad_txt = cantidad_txt.strip()  # Limpia cantidad

            if not es_float_no_negativo_simple(precio_txt):  # Valida que el precio sea correcto
                continue
            if not es_entero_no_negativo(cantidad_txt):  # Valida que la cantidad sea correcta
                continue
            if " ".join(nombre.split()) == "":  # Si el nombre está vacío, lo salta
                continue

            precio = float(precio_txt)  # Convierte el precio a número
            cantidad = int(cantidad_txt)  # Convierte cantidad a entero
            productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})  # Agrega a la lista

    return productos  # Devuelve la lista de productos cargados


# ---------- Guardar productos en el archivo ----------

def guardar_productos(nombre_archivo, productos):
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:  # Abre el archivo en modo escritura
        i = 0
        while i < len(productos):  # Recorre todos los productos
            p = productos[i]  # Toma el producto actual
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")  # Escribe en el archivo
            i += 1  # Pasa al siguiente


# ---------- Mostrar lista de productos ----------

def mostrar_productos(productos):
    print("\n--- LISTA DE PRODUCTOS ---")  # Muestra el título
    if not productos:  # Si la lista está vacía
        print("(Vacío o archivo no encontrado)")  # Muestra aviso
        return
    i = 0
    while i < len(productos):  # Recorre la lista
        p = productos[i]  # Obtiene un producto
        print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")  # Muestra info
        i += 1  # Avanza


# ---------- Agregar producto nuevo ----------

def agregar_producto(nombre_archivo):
    productos = leer_productos(nombre_archivo)  # Carga los productos existentes
    nombre = pedir_texto_no_vacio("Nombre del producto: ")  # Pide el nombre
    precio = pedir_float_no_negativo("Precio: ")  # Pide el precio
    cantidad = pedir_entero_no_negativo("Cantidad: ")  # Pide la cantidad
    productos.append({"nombre": nombre, "precio": precio, "cantidad": cantidad})  # Agrega el nuevo producto
    guardar_productos(nombre_archivo, productos)  # Guarda todos los productos
    print("Producto agregado y archivo actualizado correctamente.")  # Mensaje final


# ---------- Buscar producto por nombre ----------

def buscar_producto(productos):
    if not productos:  # Si no hay productos
        print("No hay productos cargados o el archivo no existe.")
        return
    nombre = pedir_texto_no_vacio("Ingrese el nombre del producto a buscar: ")  # Pide el nombre
    i = 0
    encontrado = False  # Marca si se encuentra el producto
    while i < len(productos):  # Recorre la lista
        p = productos[i]
        if p["nombre"].lower() == nombre.lower():  # Compara sin mayúsculas/minúsculas
            print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")  # Muestra datos
            encontrado = True
            break  # Sale del bucle
        i += 1
    if not encontrado:  # Si no se encontró
        print("El producto no existe en la lista.")


# ---------- Eliminar producto por nombre ----------

def eliminar_productos(nombre_archivo):
    productos = leer_productos(nombre_archivo)  # Carga los productos actuales
    if not productos:  # Si no hay productos
        print("No hay productos cargados o el archivo no existe.")
        return
    nombre = pedir_texto_no_vacio("Ingrese el nombre del producto a eliminar: ").lower()  # Pide el nombre
    restantes = []  # Lista para los productos no eliminados
    eliminados = 0  # Contador de eliminados
    i = 0
    while i < len(productos):  # Recorre todos los productos
        if productos[i]["nombre"].lower() != nombre:  # Si no coincide el nombre
            restantes.append(productos[i])  # Lo mantiene
        else:
            eliminados += 1  # Cuenta los eliminados
        i += 1
    if eliminados == 0:  # Si no se eliminó ninguno
        print("El producto no existe en la lista.")
        return
    guardar_productos(nombre_archivo, restantes)  # Guarda la nueva lista
    print(f"Se eliminaron {eliminados} producto(s) con el nombre indicado.")  # Mensaje final


# ---------- Menú principal ----------

def main():
    archivo = "productos.txt"  # Nombre del archivo usado
    while True:  # Bucle del menú
        print("\n===== MENÚ PRINCIPAL =====")  # Título
        print("1. Agregar producto")
        print("2. Mostrar todos los productos")
        print("3. Buscar producto por nombre")
        print("4. Eliminar producto(s) por nombre")
        print("5. Salir")
        opcion = input("Seleccione una opción (1-5): ").strip()  # Pide opción
        if opcion == "1":  # Opción 1: agregar
            agregar_producto(archivo)
        elif opcion == "2":  # Opción 2: mostrar
            productos = leer_productos(archivo)
            mostrar_productos(productos)
        elif opcion == "3":  # Opción 3: buscar
            productos = leer_productos(archivo)
            buscar_producto(productos)
        elif opcion == "4":  # Opción 4: eliminar
            eliminar_productos(archivo)
        elif opcion == "5":  # Opción 5: salir
            print("Hasta luego")
            break
        else:
            print("Opción inválida. Intente nuevamente.")  # Opción no válida


# ---------- Punto de entrada ----------
if __name__ == "__main__":  # Solo se ejecuta si el archivo es principal
    main()  # Inicia el programa

