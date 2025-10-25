# Definición de la función contar_digito que cuenta cuántas veces aparece un dígito en un número
def contar_digito(n, d):
    # Se usa abs() para asegurar que ambos sean positivos (en caso de que el usuario ingrese números negativos)
    n = abs(n)
    d = abs(d) % 10  # Si el usuario ingresa un número mayor a 9, se toma solo su último dígito

    # Caso base 1: si el número es 0, se verifica si el dígito buscado también es 0
    # En ese caso devuelve 1, de lo contrario 0
    if n == 0:
        return 1 if d == 0 else 0

    # Caso base 2: si el número tiene un solo dígito (menor que 10)
    # se compara directamente con el dígito buscado
    if n < 10:
        return 1 if n == d else 0

    # Caso recursivo:
    # Se compara el último dígito del número (n % 10) con el dígito buscado (d)
    # Si son iguales, suma 1; si no, suma 0
    # Luego llama recursivamente a la función con el número sin su último dígito (n // 10)
    return (1 if (n % 10) == d else 0) + contar_digito(n // 10, d)


# Bloque principal del programa: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    # Pide al usuario que ingrese un número entero
    numero = int(input("Ingrese un número: "))
    
    # Pide al usuario que ingrese el dígito que quiere contar dentro del número
    digito = int(input("Ingrese el dígito a contar: "))
    
    # Llama a la función contar_digito y muestra cuántas veces aparece el dígito en el número
    print(f"El dígito {digito} aparece {contar_digito(numero, digito)} veces en {numero}.")
