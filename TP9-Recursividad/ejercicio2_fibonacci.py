# Definición de la función fibonacci que calcula el término n de la serie
def fibonacci(n):
    # Caso base 1: si n es 0, devuelve 0 (primer número de la serie)
    if n == 0:
        return 0
    # Caso base 2: si n es 1, devuelve 1 (segundo número de la serie)
    if n == 1:
        return 1
    # Caso recursivo: el término n es la suma de los dos anteriores
    return fibonacci(n - 1) + fibonacci(n - 2)


# Definición de la función serie_fibonacci que genera la lista completa hasta n
def serie_fibonacci(n):
    # Caso base: si n es 0, devuelve una lista con un solo elemento [0]
    if n == 0:
        return [0]
    # Llamada recursiva: obtiene la serie hasta n - 1
    prev = serie_fibonacci(n - 1)
    # Calcula el término n de la serie y lo agrega al final de la lista
    prev.append(fibonacci(n))
    # Devuelve la lista completa con todos los términos desde 0 hasta n
    return prev


# Bloque principal: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    # Pide al usuario que ingrese un número (cantidad de términos)
    num = int(input("Ingrese la cantidad de términos: "))
    
    # Imprime la lista completa de la serie de Fibonacci hasta el número ingresado
    print(f"Serie de Fibonacci hasta {num}: {serie_fibonacci(num)}")
