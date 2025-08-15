#4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y
#su perímetro.


radio= float(input("ingrese el radio de un circulo y le diremos su área y perimetro\n"))
area= 3.14 * (radio** 2)
perimetro = 2 * 3.14 * radio

# Resultados
print(f"El área del círculo es: {area:.2f}")
print(f"El perímetro del círculo es: {perimetro:.2f}")