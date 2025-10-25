# Definición de la función factorial
def factorial(n):
    # Si el número es 0, el factorial por definición es 1 (caso base)
    if n == 0:
        return 1
    # En cualquier otro caso, multiplica n por el factorial del número anterior
    return n * factorial(n - 1)


# Definición de la función factoriales_hasta
def factoriales_hasta(n):
    # Caso base: si n es 1, devuelve una lista con el factorial de 1 (que es 1)
    if n == 1:
        return [1]
    
    # Llamada recursiva: obtiene la lista de factoriales hasta n-1
    prev = factoriales_hasta(n - 1)
    
    # Calcula el factorial de n usando la función factorial() y lo agrega a la lista
    prev.append(factorial(n))
    
    # Devuelve la lista completa con los factoriales desde 1 hasta n
    return prev


# Bloque principal del programa: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    # Pide al usuario que ingrese un número entero y lo convierte a int
    num = int(input("Ingrese un número: "))
    
    # Imprime el factorial del número ingresado llamando a la función factorial
    print(f"Factorial de {num}: {factorial(num)}")
    
    # Imprime la lista de factoriales desde 1 hasta el número ingresado
    print(f"Factoriales hasta {num}: {factoriales_hasta(num)}")

