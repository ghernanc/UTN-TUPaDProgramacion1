# Ejercicio 9 - Convertir grados Celsius a Fahrenheit.

def celsius_a_fahrenheit(celsius):  # Definimos la función con el parámetro 'celsius'.
    # Fórmula de conversión: (°C * 9/5) + 32
    # En Python los parámetros se pasan por referencia a objetos.
    # En este caso usamos números (tipos inmutables), por lo que se comportan como pasados por valor.
    return (celsius * 9 / 5) + 32  # Devuelve el valor convertido a grados Fahrenheit.

# Solicitamos al usuario que ingrese la temperatura en grados Celsius.
# Usamos float() para permitir números con decimales.
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# f crea una f-string, { } insertan variables dentro del texto y .2f muestra 2 decimales.
print(f"Temperatura en Fahrenheit: {celsius_a_fahrenheit(celsius):.2f}")
