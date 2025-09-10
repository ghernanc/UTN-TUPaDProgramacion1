#2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
#dígitos que contiene.
#Metodo 1
numero = int(input("Ingrese un numero entero: "))

# Pasamos a positivo por si el número es negativo con la funcion absoluto.
#Si no hago eso cuenta el guion como caracter.
numero = abs(numero)

# Cuento los digitos convirtiendo el numero en cadena
cantidad_digitos = len(str(numero))

print("El numero ingresado tiene", cantidad_digitos, "digitos.")

