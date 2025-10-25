# Definición de la función suma_digitos
# Calcula la suma de los dígitos de un número entero usando recursión.
def suma_digitos(n):
    # Convierte el número a positivo por si el usuario ingresa un número negativo
    n = abs(n)
    
    # Caso base:
    # Si el número tiene un solo dígito (es menor que 10),
    # la suma de sus dígitos es él mismo.
    if n < 10:
        return n
    
    # Caso recursivo:
    # Suma el último dígito (n % 10)
    # con la suma de los dígitos del resto del número (n // 10)
    return (n % 10) + suma_digitos(n // 10)


# Bloque principal: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    # Pide al usuario que ingrese un número entero
    numero = int(input("Ingrese un número: "))
    
    # Llama a la función y muestra el resultado de la suma de los dígitos
    print(f"La suma de los dígitos de {numero} es {suma_digitos(numero)}")
