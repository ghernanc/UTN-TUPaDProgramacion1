#7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
#número entero positivo indicado por el usuario.

print("Ingrese un numero y se sumaran todo los comprendidos entre 0 y el numero indicado")

num = int(input("Ingrese el  numero: "))


suma = 0


for i in range( 1, num+1): #Agrego +1 a num porque sino lo excluye. La funcion Range va de 1 a num +1.
    suma += i   #voy sumando a medida que i aumenta hata llegar a num +1.

print("La suma de los numeros comprendidos entre", 0, "y", num, "es:", suma)

