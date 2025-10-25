# Definición de la función contar_bloques
# Calcula la cantidad total de bloques necesarios para construir una pirámide de n niveles.
# Cada nivel tiene una cantidad de bloques igual a su número de nivel.
# Ejemplo: para n = 4 → 1 + 2 + 3 + 4 = 10 bloques.
def contar_bloques(n):
    # Caso base:
    # Si n es 0 o 1, devuelve n (0 bloques si no hay niveles, 1 bloque si hay un solo nivel)
    # Se usa max(0, n) para evitar resultados negativos en caso de que n < 0.
    if n <= 1:
        return max(0, n)
    
    # Caso recursivo:
    # Suma el número de bloques del nivel actual (n)
    # más el total de bloques de todos los niveles anteriores (n - 1)
    return n + contar_bloques(n - 1)


# Bloque principal: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    # Pide al usuario que ingrese la cantidad de niveles de la pirámide
    niveles = int(input("Ingrese el número de niveles: "))
    
    # Llama a la función y muestra el total de bloques necesarios
    print(f"Total de bloques necesarios: {contar_bloques(niveles)}")
