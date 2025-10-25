# Definición de la función decimal_a_binario que convierte un número decimal a binario usando recursión
def decimal_a_binario(n):
    # Caso base 1: si el número es 0, su representación binaria es "0"
    if n == 0:
        return "0"
    # Caso base 2: si el número es 1, su representación binaria es "1"
    if n == 1:
        return "1"
    # Caso recursivo:
    # Se divide el número por 2 (división entera) y se llama nuevamente a la función
    # Luego se concatena el resto (n % 2), que será 0 o 1, al final de la cadena resultante
    # Así, los restos se van acumulando en el orden correcto para formar el número binario completo
    return decimal_a_binario(n // 2) + str(n % 2)


# Bloque principal del programa: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    # Pide al usuario que ingrese un número entero decimal
    num = int(input("Ingrese un número decimal: "))
    
    # Llama a la función y muestra en pantalla el número convertido a binario
    print(f"El número {num} en binario es: {decimal_a_binario(num)}")
