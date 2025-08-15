#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de
#multiplicar de dicho número.

numero = int(input("Ingrese un número: "))
i = 1

while i <= 10:
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
    i += 1