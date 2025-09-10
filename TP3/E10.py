#10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
#usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

num = int(input("Ingrese un número: "))

invertido = 0

# Guardo el numero si es negativo (True o False)
es_negativo = num < 0

# valor absoluto del numero para trabajar solo con los digitos positivos.
num = abs(num)

# Mientras el numero tenga digitos.
while num > 0:
    # Tomo el ultimo digito.
    resto = num % 10

    # Lo agrego al número invertido, desplazando lo que había 
    # antes una posición a la izquierda (*10)
    invertido = invertido * 10 + resto

    # Le saco el ultimo digito al nmuero original usando division entera
    num = num // 10

# Si el numero original era negativo, le pongo el signo
if es_negativo:
    invertido = -invertido


print("Numero invertido:", invertido)


