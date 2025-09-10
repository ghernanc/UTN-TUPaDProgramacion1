#9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
#media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
#poder procesar 100 números cambiando solo un valor).

print("Ingrese números enteros y le indicaremos la media. ")

# Contadores
suma = 0
num= 0
media=0
cant=10 # Puedo cambiar el 10 por la cantidad que se quiera ingresar.
 


for i in range(cant): # va del 0 al 9.
    num = int(input(f"Ingrese el numero {i+1}: ")) #f indica que es una f-string (cadena). Es para interpretar lo que esta entre llaves.
                                                   #{i+1} muestra el valor actual i más 1.
                                                   #Como el bucle for empieza en 0, el primer mensaje seria "Ingrese el número 0:" y estaria mal.
    suma = suma+num
media  = suma/cant    
print("La media de los numeros ingresados es:", media)

