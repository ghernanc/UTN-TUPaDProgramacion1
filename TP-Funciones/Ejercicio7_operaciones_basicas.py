# Ejercicio 7 - Suma, resta, multiplicación y división de dos números.

def operaciones_basicas(a, b):  # Definimos la función con dos parámetros.
    # Realizamos las cuatro operaciones básicas.
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = None  # Inicializamos en None por si b es 0.
    if b != 0:  # Evitamos dividir por cero.
        division = a / b

    # Mostramos los resultados dentro de la función.
    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    if division is None: #es un valor especial que significa "sin resultado" o "vacío".
                         # Se usa para indicar que no se pudo realizar la división.
        print("División: no se puede dividir por cero.")
    else:
        print(f"División: {division}")

# Solicitamos dos números al usuario.
# Usamos float() para permitir decimales y evitar errores con la división.
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))

# Llamamos a la función pasando los valores ingresados como argumentos.
operaciones_basicas(a, b)
