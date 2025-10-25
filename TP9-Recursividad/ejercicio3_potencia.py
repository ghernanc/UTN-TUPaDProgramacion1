# Definición de la función potencia que calcula base elevado a exponente
def potencia(base, exp):
    # Caso base: cualquier número elevado a 0 es 1
    if exp == 0:
        return 1
    # Caso recursivo: multiplica la base por la potencia de (exp - 1)
    
    return base * potencia(base, exp - 1)


# Bloque principal: se ejecuta solo si el archivo se corre directamente
if __name__ == "__main__":
    # Pide al usuario que ingrese la base y la convierte a número decimal (float)
    base = float(input("Ingrese la base: "))
    
    # Pide al usuario que ingrese el exponente y lo convierte a número entero
    exp = int(input("Ingrese el exponente: "))
    
    # Muestra el resultado de elevar la base al exponente, llamando a la función potencia
    print(f"{base}^{exp} = {potencia(base, exp)}")
