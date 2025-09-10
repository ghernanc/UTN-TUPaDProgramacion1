
#8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
#programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
#negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
#menor, pero debe estar preparado para procesar 100 números con un solo cambio).

print("Ingrese números y le indicaremos cuántos son pares, impares, negativos , positivos")

# Contadores
pos = 0
neg = 0
par = 0
imp = 0
ceros = 0

# Puede cambiar el 10 por la cantidad que se desee ingresar.
for i in range(10):
    num = int(input(f"Ingrese el numero {i+1}: ")) #f indica que es una f-string (cadena). Es para interpretar lo que esta entre llaves.
                                                   #{i+1} muestra el valor actual i más 1.
                                                   #Como el bucle for empieza en 0, el primer mensaje seria "Ingrese el número 0:" y estaria mal.

    if num > 0:
        pos += 1
    elif num < 0:
        neg += 1
    else:
        ceros += 1  # el 0 es neutro y par

    if num % 2 == 0:
        par += 1
    else:
        imp += 1

# Resultados
print("cantidad de pares:", par)
print("cantidad de impares:", imp)
print("cantidad de positivos:", pos)
print("cantidad de negativos:", neg)
print("cantidad de ceros:", ceros) #como el 0 no es negativo ni positivo lo cuento aparte.
