# Ejercicio 6 - Mostrar tabla de multiplicar del 1 al 10.

def tabla_multiplicar(numero):  # Definimos la función con el parámetro 'numero'.
    # Recorremos los valores del 1 al 10 usando un bucle for.
    for i in range(1, 11):
        # Mostramos la operación con una f-string para incluir variables dentro del texto.
        # { } indican dónde se insertan los valores de las variables.
        print(f"{numero} x {i} = {numero * i}")

    # Solicitamos al usuario que ingrese un número entero para generar la tabla.
     #Usamos int() para convertir el texto ingresado por input() a número entero,
    # ya que vamos a realizar operaciones matemáticas (multiplicaciones).
numero = int(input("Ingrese un número para mostrar su tabla de multiplicar: "))
    

tabla_multiplicar(numero) # Llamamos a la función pasando el número ingresado como argumento.


