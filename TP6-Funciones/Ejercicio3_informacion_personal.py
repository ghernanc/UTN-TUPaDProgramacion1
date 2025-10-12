# Ejercicio 3 - Función que imprime información personal

def informacion_personal(nombre, apellido, edad, residencia): # Definimos la función con cuatro parámetros.
    
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}") # Muestra los datos personales combinados en un texto.

# Solicitamos los datos personales al usuario con la función input().
# No es necesario convertir a número porque no realizamos operaciones con valores enteros.

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
edad = input("Ingrese su edad: ")
residencia = input("Ingrese su lugar de residencia: ")
informacion_personal(nombre, apellido, edad, residencia) # Llamamos a la función pasando los datos ingresados como argumentos.
