# Ejercicio 4 - Calcular área y perímetro de un círculo.

import math  # Importamos el módulo math para poder usar el valor de pi (π).

def calcular_area_circulo(radio):  # Definimos la función con el parámetro 'radio'.
    # Devuelve el área del círculo usando la fórmula: π * r²
    return math.pi * (radio ** 2)  # Calcula el área multiplicando pi por el cuadrado del radio.

def calcular_perimetro_circulo(radio):  # Definimos otra función con el mismo parámetro 'radio'.
    # Devuelve el perímetro del círculo usando la fórmula: 2 * π * r
    return 2 * math.pi * radio  # Calcula el perímetro multiplicando 2 por pi y por el radio.

# Pedimos al usuario que ingrese el valor del radio y lo convertimos a número decimal.
r = float(input("Ingrese el radio del círculo: "))

# Mostramos los resultados con dos decimales.
print(f"Área: {calcular_area_circulo(r):.2f}")        # Llama a la función y muestra el área.
print(f"Perímetro: {calcular_perimetro_circulo(r):.2f}")  # Llama a la función y muestra el perímetro.


