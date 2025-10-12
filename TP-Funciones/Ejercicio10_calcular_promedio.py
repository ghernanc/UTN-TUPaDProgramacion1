# Ejercicio 10 - Calcular el promedio de tres números.

def calcular_promedio(a, b, c):  # Definimos la función con tres parámetros.
    # En Python los parámetros se pasan por referencia a objetos.
    # En este caso usamos números (tipos inmutables), por lo que se comportan como pasados por valor.
    
    # Sumamos los valores y dividimos por 3.
    return (a + b + c) / 3  # Devuelve el resultado del promedio.

# Solicitamos los tres números al usuario.
# Usamos float() para permitir números con decimales.
a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
c = float(input("Ingrese el tercer número: "))

# f crea una f-string, { } insertan variables dentro del texto y .2f muestra el resultado con 2 decimales.
print(f"El promedio es: {calcular_promedio(a, b, c):.2f}")
